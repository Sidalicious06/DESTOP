from PySide6.QtWidgets import QMainWindow, QMenu, QGraphicsOpacityEffect
from PySide6.QtGui import QAction
from PySide6.QtCore import QProcess
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QGraphicsOpacityEffect
from PySide6.QtCore import QTimer
from PySide6.QtCore import QSettings

import time
import seaborn as sns
import pandas as pd

from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from PySide6.QtWidgets import QVBoxLayout

import cv2
import sys
import csv

from ui_index import Ui_MainWindow
from modulation_handler import VerificationOverlay

completeBlinkCount = 0
incompleteBlinkCount = 0
totalBlinkCount = 0

baseline_blink_frequency = 17 #blinks per minute




class DESTOPControl(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("DESTOP")



        # Start on Control Panel
        self.stackedWidget.setCurrentIndex(0)

        
    
        self.overlay = VerificationOverlay()
    
        self.detector = QProcess(self)

        self.oculomotor_running = False

        self.detector.setProgram(sys.executable)
        self.detector.setArguments([
            "-u",  
            "blink.py"
        ])





        self.detector.start()


        self.graph_figure = Figure(figsize=(6, 4))
        self.graph_canvas = FigureCanvasQTAgg(self.graph_figure)

        self.graph_layout = QVBoxLayout(self.Graph)
        self.graph_layout.setContentsMargins(0, 0, 0, 0)
        self.graph_layout.addWidget(self.graph_canvas)

        self.graph_ax = self.graph_figure.add_subplot(111)

        self.metric_history = []


        self.graph_2_figure = Figure()
        self.graph_2_canvas = FigureCanvasQTAgg(self.graph_2_figure)

        self.graph_2_layout = QVBoxLayout(self.Graph_2)
        self.graph_2_layout.setContentsMargins(0, 0, 0, 0)
        self.graph_2_layout.addWidget(self.graph_2_canvas)

        self.graph_2_ax = self.graph_2_figure.add_subplot(111)




        self.duration_history = []
        

        self.fluctuation_timer = QTimer(self)
        self.fluctuation_timer.setSingleShot(True)
        self.fluctuation_timer.timeout.connect(self.trigger_next_fluctuation)

        self.fluctuation_interval_ms = 5000  
        self.fluctuation_intensity = 38

        

    # Subprocess Reading
    
        self.detector.readyReadStandardOutput.connect(self.read_detector_output)

        self.detector.readyReadStandardError.connect(self.read_detector_errors)

        self.detector.finished.connect(self.detector_finished)
    
    # Switching Pages

        self.ControlPanelButton.clicked.connect(self.switch_to_control_panel_page)
        self.ControlPanelIcon.clicked.connect(self.switch_to_control_panel_page)

        # self.ModulationButton.clicked.connect(self.switch_to_modulation_page)
        # self.ModulationIcon.clicked.connect(self.switch_to_modulation_page)

        self.DashboardButton.clicked.connect(self.switch_to_dashboard_page)
        self.DashboardIcon.clicked.connect(self.switch_to_dashboard_page)

        self.AboutButton.clicked.connect(self.switch_to_about_page)
        self.AboutIcon.clicked.connect(self.switch_to_about_page)

        # self.SettingsButton.clicked.connect(self.switch_to_settings_page)
        # self.SettingsIcon.clicked.connect(self.switch_to_settings_page)

        self.ExitIcon.clicked.connect(self.exit)
        self.QuitButton.clicked.connect(self.exit)

        self.PowerButton.toggled.connect(self.oculomotor_toggle)

    def send_command(self, command: str):
        if self.detector.state() != QProcess.ProcessState.Running:
            print("Detector process is not running")
            return

        self.detector.write((command + "\n").encode("utf-8"))

    

    def switch_to_control_panel_page(self):
        self.stackedWidget.setCurrentIndex(0)

    # def switch_to_modulation_page(self):
    #     self.stackedWidget.setCurrentIndex(1)    

    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(2)

    # def switch_to_settings_page(self):
    #     self.stackedWidget.setCurrentIndex(3)

    def switch_to_about_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def exit(self):

        
        self.overlay.stop_fluctuation()
        
        self.send_command("exit")
        self.close()


    def read_detector_output(self):

       
        global completeBlinkCount, incompleteBlinkCount, totalBlinkCount
        global baseline_blink_frequency

        data = bytes(
            self.detector.readAllStandardOutput()
        ).decode("utf-8", errors="replace")

        for line in data.splitlines():
            message = line.strip()

            if not message:
                continue

            print("Detector:", message)

            if message == "PYTHON_READY":
                oculomotor_ready = True
                self.PowerButton.setEnabled(True)
                self.StatusIndicator.setText("STATUS: READY")

            elif message == "LOOP STARTED":
                self.oculomotor_running = True
                self.StatusIndicator.setText("STATUS: RUNNING")
                self.fluctuation_timer.start(self.fluctuation_interval_ms)
            elif message == "ACK_STOP":
                self.overlay.stop_fluctuation()
                self.oculomotor_running = False
                self.StatusIndicator.setText("STATUS: PAUSED")
            elif message == "ACK_EXIT":

                self.oculomotor_running = False
                self.StatusIndicator.setText("STATUS: CLOSING...")
            elif message.startswith("REPORT"):

                msg = message.split()
                
                complete_score = float(msg[1])
                incomplete_score = float(msg[2])
                duration = float(msg[3]) * 1000
                if duration > 600:
                    duration = 600
                time = msg[4]
                
                if complete_score > .37:
                    print("complete")
                    state = "complete"
                    completeBlinkCount += 1
                    
                else:
                    print("incomplete")
                    state = "incomplete"
                    incompleteBlinkCount += 1


                self.duration_history.append({
                    "blink_duration_ms": duration,
                    "blink_type": state,
                })

                dfDuration = pd.DataFrame(self.duration_history)
                self.plot_blink_duration_violin(dfDuration)
                

                # data = [state, complete_score, incomplete_score, duration, time]
                
                # with open('graphingData', mode='a', newline='', encoding='utf-8') as file:
                #     writer = csv.writer(file)
                #     writer.writerow(data)  # Appends the single row


            elif message.startswith("EVALUATE"):
                print("ACK_EVALUATE")

                msg = message.split()

                totalBlinkCount = incompleteBlinkCount + completeBlinkCount
                recent_frequency = totalBlinkCount * 2
                

                self.metric_history.append({
                    "timestamp": int(float(msg[1])),
                    "blink_rate": recent_frequency,
                })

                df = pd.DataFrame(self.metric_history)
                self.plot_blink_data(df)



                if recent_frequency < baseline_blink_frequency - 3:
                    print("Intensifying...")

                    self.fluctuation_interval_ms -= 500
                    self.fluctuation_intensity += 8

                elif recent_frequency > baseline_blink_frequency + 3:
                    print("Relaxing...")

                    self.fluctuation_interval_ms += 500
                    self.fluctuation_intensity -= 8

                else:
                    print("Nominal! Don't change anything :)")

                totalBlinkCount = 0
                incompleteBlinkCount = 0
                completeBlinkCount = 0


                

    def schedule_next_fluctuation(self):
        
        if not self.oculomotor_running:
            return

        
        self.fluctuation_timer.start(
            self.fluctuation_interval_ms
        )

    def trigger_next_fluctuation(self):
        
        if not self.oculomotor_running:
            return

        

        self.overlay.trigger_fluctuation(1500, self.fluctuation_intensity, 4, 200 )

        self.schedule_next_fluctuation()


    def plot_blink_data(self, df):
        self.graph_ax.clear()

        sns.lineplot(
            data=df,
            x="timestamp",
            y="blink_rate",
            ax=self.graph_ax,
        )

        self.graph_ax.set_title("Real-Time Blink Rate")
        self.graph_ax.set_xlabel("Time")
        self.graph_ax.set_ylabel("Blinks per Minute")
        self.graph_ax.axhspan(
            15, 20,
            alpha=0.15,
            color="green",
            label="Target range",
        )
        self.graph_ax.legend()
        self.graph_figure.tight_layout()
        self.graph_canvas.draw_idle()

            


  

    def oculomotor_toggle(self):
        

        if self.oculomotor_running:
            self.send_command("stop")
            
            
        else:
            self.send_command("START")
            

    def plot_blink_duration_violin(self, df):
        if df.empty:
            return

        required = {"blink_duration_ms", "blink_type"}
        if not required.issubset(df.columns):
            return

        plot_df = df[
            df["blink_type"].isin(["complete", "incomplete"])
        ].copy()

        plot_df["blink_duration_ms"] = pd.to_numeric(
            plot_df["blink_duration_ms"], errors="coerce"
        )
        plot_df = plot_df.dropna(
            subset=["blink_duration_ms", "blink_type"]
        )

        if plot_df.empty:
            return

        self.graph_2_ax.clear()

        sns.violinplot(
            data=plot_df,
            x=[""] * len(plot_df),
            y="blink_duration_ms",
            hue="blink_type",
            hue_order=["complete", "incomplete"],
            split=True,
            inner="box",
            cut=0,
            ax=self.graph_2_ax,
        )

        self.graph_2_ax.set_title("Blink Duration Distribution")
        self.graph_2_ax.set_xlabel("")
        self.graph_2_ax.set_ylabel("Blink Duration (ms)")
        self.graph_2_ax.legend(title="Blink Type")

        self.graph_2_figure.tight_layout()
        self.graph_2_canvas.draw_idle()



    def read_detector_errors(self):
        data = bytes(
            self.detector.readAllStandardError()
        ).decode("utf-8", errors="replace")

        if data.strip():
            print("Detector error/log:", data)


    def detector_finished(self, exit_code, exit_status):
        self.detector_running = False
        print(f"Detector exited: code={exit_code}")


