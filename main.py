from config import data

from kivy.uix.accordion import ObjectProperty
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.config import Config

from requests import *
from bs4 import BeautifulSoup
from time import time


Config.set('kivy', 'keyboard_mode', 'systemanddock')


class root(FloatLayout):
    @staticmethod
    def BTC_switch_function():
        return data["BTC_switch"]
    
    def BTC_switch_check(self, checkbox, value, heigh_price, low_price):
        data["BTC_switch"] = value
        with open('YoBit парсер/config.py', 'w') as file:
            file.write(f'data = {str(data)}')
        if value: #? TRUE
            request = get(url='https://yobit.net/ru/trade/BTC/USDT').text
            soup = BeautifulSoup(request, 'lxml')
            last_price_BTC = soup.find("span", id='label_last').text

class YoBitAlertApp(MDApp):
    def build(self):
        return root()

if __name__ == "__main__":
    YoBitAlertApp().run()