from requests import get

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("weather-ui.ui")
token = "801db4d874c0fd13fadef4c681a48929"


class App(QtWidgets.QMainWindow, Form):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        city_name = self.cityField.toPlainText()
        json = get("https://api.openweathermap.org/data/2.5/weather", {
            "q": city_name,
            "appid": token,
            "units": "metric",
            "lang": "ru"
        }).json()
        self.temperatureLabel.setText(str(json["main"]["temp"]))


app = QApplication([])
window = App()
window.show()
app.exec_()