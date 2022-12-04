class Car():
    __brand = ""
    __model = ""
    __price = 0.
    __power = 0
    __currency = ""


    def __str__(self):
        return f"{self.brand}, {self.model}, HP={self.power}, price={self.price} {self.currency}"

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value: str):
        if len(value) > 0 and value[0].isalpha():
            self.__brand = value.capitalize()
        else:
            raise AttributeError("Brand name require at least one letter")

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value: str):
        if len(value) > 0 and value[0].isalpha():
            self.__model = value.capitalize()
        else:
            raise AttributeError("Model name require at least one letter")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value > 1000:
            self.__price = value
        else:
            raise AttributeError("Price should be at least 1000")

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value: int):
        if value > 74:
            self.__power = value
        else:
            raise AttributeError("Power should be at least 75 HP")

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value: str):
        import re
        pattern = "\D{3}"
        if re.search(pattern, value):
            self.__currency = value.upper()
        else:
            raise AttributeError("Price should be at least 1000")
