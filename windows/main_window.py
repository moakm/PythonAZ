import pymongo
import requests
from PyQt6.QtWidgets import *
from PyQt6 import uic
import os

from lib.utils.utils_validators import isnumber


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(rf"{os.getcwd()}\lib\gui\demo_interface.ui", self)

        self.__interface()
        self.show()
        self.__filldata()
        self.currency_price = 0

    def __interface(self):
        self.label = self.findChild(QLabel, 'label_fname')
        self.lbl_currency_price = self.findChild(QLabel, 'lbl_currency_price')
        self.fname = self.findChild(QLineEdit, 'txt_fname')
        self.btn_submit = self.findChild(QPushButton, 'btn_submit')
        self.cmb_currency_codes = self.findChild(QComboBox, 'comboBox_currency_codes')
        self.btn_transaction_save = self.findChild(QPushButton, 'btn_transaction_save')

        # Action assign to object - button onclick
        self.btn_submit.clicked.connect(self.demo_action)
        self.btn_transaction_save.clicked.connect(self.__mongodb_save)

    def demo_action(self):
        self.user_input_txt = self.fname.text()
        if isnumber(self.user_input_txt.replace(",", ".")):
            self.currency_code = self.cmb_currency_codes.currentText()
            url = rf"http://api.nbp.pl/api/exchangerates/rates/A/{self.currency_code}/?format=json"
            try:
                response = requests.get(url)
                response_json = response.json()
                self.exchange_rate = response_json.get('rates')[0].get('mid')
                self.currency_price = float(self.user_input_txt.replace(',', '.')) / self.exchange_rate
                self.lbl_currency_price.setText(f"{self.currency_price:.2f} {self.currency_code}")
            except Exception as e:
                print(e)
        else:
            self.label.setText(f"Hello {self.fname.text()}")

    def __filldata(self):
        import requests
        url = r"http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
        try:
            response = requests.get(url)
            response_json = response.json()
            currency_data = response_json[0].get("rates")
            [self.cmb_currency_codes.addItem(k.get("code")) for k in currency_data]
        except:
            print("Something went wrong.")

    def __mongodb_save(self):
        import datetime as dt

        self.price_pln = float(self.fname.text().replace(',', '.'))
        self.date = dt.datetime.now()
        self.time = self.date.strftime("%H:%M:%S")
        self.date = self.date.strftime("%Y-%m-%d")

        client = pymongo.MongoClient("mongodb://localhost:27017")
        database = client["operation_register"]
        collection = database["transactions"]

        # Insert operation
        input_data = collection.insert_one(
            {
                "PLN_price": self.price_pln,
                "currency": self.cmb_currency_codes.currentText(),
                "value": self.currency_price,
                "date": self.date,
                "time": self.time
            }
        )
