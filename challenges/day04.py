# try to project class Car
# HP > 0
# price > 1000
# currency 3 upper letters
from lib.classes.car import Car
from lib.utils.util_console_mgmt import cls


def c06_classes():
    toyota = Car()
    toyota.brand = 'toyota'
    toyota.model = 'yaris'
    toyota.power = 80
    toyota.price = 12000
    toyota.currency = 'PLN'
    print(toyota)
    cls()
