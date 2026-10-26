import sys
import random
import math
import win32con
import win32gui

from PySide6.QtCore import Qt, QTimer, QElapsedTimer
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QApplication, QMainWindow


class VerificationOverlay(QMainWindow):
    """
    Full-screen click-through brightness-negative stimulus overlay.

    intensity: target black overlay alpha, 0..255.
    longevity_ms: total duration of one fluctuation (fade-in + fade-out).
    intensity_variance: maximum random +/- alpha variation per trigger.
    longevity_variance_ms: maximum random +/- duration variation per trigger.
    """

    def __init__(
        self,
        intensity=76,
        longevity_ms=1200,
        intensity_variance=5,
        longevity_variance_ms=100,
    ):
        super().__init__()

        self.base_intensity = self._clamp(intensity, 0, 255)
        self.base_longevity_ms = max(2, int(longevity_ms))
        self.intensity_variance = max(0, int(intensity_variance))
        self.longevity_variance_ms = max(0, int(longevity_variance_ms))

        self._current_alpha = 0
        self._active_intensity = self.base_intensity
        self._active_longevity_ms = self.base_longevity_ms
        self._elapsed = QElapsedTimer()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        # The overlay starts hidden and only appears for a stimulus.
        self._timer = QTimer(self)
        self._timer.setInterval(16)  # ~60 Hz
        self._timer.timeout.connect(self._update_fluctuation)

    @staticmethod
    def _clamp(value, low, high):
        return max(low, min(high, int(value)))

    def showEvent(self, event):
        super().showEvent(event)
        self.enable_click_through()

    def enable_click_through(self):
        hwnd = int(self.winId())
        styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        win32gui.SetWindowLong(
            hwnd,
            win32con.GWL_EXSTYLE,
            styles | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT,
        )

    def trigger_fluctuation(
        self,
        longevity_ms=None,
        intensity=None,
        intensity_variance=None,
        longevity_variance_ms=None,
    ):
        """
        Start one fluctuation. Each trigger receives a small, independent
        random variation around the supplied or configured base parameters.
        Calling again while active restarts the current fluctuation.
        """
        base_intensity = self.base_intensity if intensity is None else self._clamp(intensity, 0, 255)
        base_longevity = self.base_longevity_ms if longevity_ms is None else max(2, int(longevity_ms))

        i_var = (
            self.intensity_variance
            if intensity_variance is None
            else max(0, int(intensity_variance))
        )
        t_var = (
            self.longevity_variance_ms
            if longevity_variance_ms is None
            else max(0, int(longevity_variance_ms))
        )

        # Randomize both values slightly for each event; clamp to valid ranges.
        self._active_intensity = self._clamp(
            base_intensity + random.randint(-i_var, i_var), 0, 255
        )
        self._active_longevity_ms = max(
            2, base_longevity + random.randint(-t_var, t_var)
        )

        if self._active_intensity == 0:
            self.stop_fluctuation()
            return

        if not self.isVisible():
            self.showFullScreen()
            self.enable_click_through()

        self._current_alpha = 0
        self._elapsed.start()
        self._timer.start()
        self.update()

    def stop_fluctuation(self):
        """Immediately clear the effect and hide the overlay."""
        self._timer.stop()
        self._current_alpha = 0
        self.update()
        self.hide()

    def _update_fluctuation(self):
        elapsed_ms = self._elapsed.elapsed()
        progress = elapsed_ms / self._active_longevity_ms

        if progress >= 1.0:
            self.stop_fluctuation()
            return

        # Smooth sine envelope: transparent -> peak -> transparent.
        # This preserves the requested total longevity.
        envelope = math.sin(math.pi * progress)
        self._current_alpha = round(self._active_intensity * envelope)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0, 0, 0, self._current_alpha))
        painter.end()

    def closeEvent(self, event):
        # Ensure no timer continues after the overlay is closed.
        self._timer.stop()
        self._current_alpha = 0
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = VerificationOverlay(
        intensity=76,
        longevity_ms=1200,
        intensity_variance=5,       # Random +/- 5 alpha per fluctuation
        longevity_variance_ms=100,  # Random +/- 100 ms per fluctuation
    )

    # Optional standalone test: one fluctuation, then exit after the effect ends.
    # In the integrated app, create the overlay in the GUI process and call
    # trigger_fluctuation() when the phase manager requests a stimulus.
    overlay.trigger_fluctuation()
    overlay._timer.timeout.connect(
        lambda: app.quit() if not overlay.isVisible() else None
    )
    app.aboutToQuit.connect(overlay.stop_fluctuation)

    # In your main GUI, use the same QApplication and connect its aboutToQuit
    # signal to overlay.stop_fluctuation. If the overlay is a child process
    # instead, the parent must terminate that process when its window closes.
    sys.exit(app.exec())
