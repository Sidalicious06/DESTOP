from PySide6.QtWidgets import QApplication
from frontPage import DESTOPControl
import sys
import blink

app = QApplication(sys.argv)

window = DESTOPControl()

window.show()
app.exec()  