class Person():
    __first_name = ""
    __last_name = ""
    __pesel = ""

    def __init__(self, firstname:str, lastname:str):
        self.first_name = firstname
        self.set_last_name(lastname)

    def __str__(self):
        return f"{self.first_name} {self.get_last_name()}, {self.pesel}, {self.gender}"

    # Akcesory - specjalne funkcje zapewniające dostęp
    # do elementów prywatnych

    # Read accessor
    @property #dekorator modyfikujący działanie funkcji do postaci akcesora(właściwości)
    def first_name(self):
        '''
        read
        :return:
        '''
        return self.__first_name

    # write accessor
    @first_name.setter
    def first_name(self, value:str):
        '''
        create and write accessor
        :param value:
        :return:
        '''
        if len(value) > 0 and value[0].isalpha():
            self.__first_name = value
        else:
            raise AttributeError("First name require at least one letter")

    # Function type accessors
    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, value:str):
        if len(value) > 0 and value[0].isalpha():
            self.__last_name = value
        else:
            raise AttributeError("Last name require at least one letter")
    @property
    def pesel(self):
        return self.__pesel
    @pesel.setter
    def pesel(self, value:str):
        import re
        pattern = "\d{11}"
        if re.search(pattern, value): self.__pesel = value
        else: raise AttributeError('Pesel require 11 digits.')

    @property
    def gender(self):
        if len(self.pesel) >0:
            return "W" if int(self.pesel[9]) % 2 == 0 else "M"
        else:
            raise AttributeError("Pesel missing, not able to generate gender")

    @staticmethod
    def bmi(weight: float, height: float):
        return weight / (height * 2)

    pass
