from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("weather-ui.ui")


class App(QtWidgets.QMainWindow, Form):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        print("click")


app = QApplication([])
window = App()
window.show()
app.exec_()
