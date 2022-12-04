class Studia:
    __academy_structure={
        "eletronika": ["automatyka", "elektronika"],
        "mechaniczny":["mechaniczny", "robotyka"],
        "it":["systemy operacyjne", "bazy danych", "mikroprocesory"]
    }
    __wydzial = ""
    __kierunek = ""
    __nr_indeks = ""

    def __init__(self, wydzial:str, kierunek:str, nr_indeks:str):
        self.wydzial = wydzial
        self.kierunek = kierunek
        self.nr_indeks = nr_indeks

    def __str__(self):
        return f"studiuje na wydziale {self.wydzial}, na kierunku {self.kierunek}"

    @property
    def wydzial(self):
        return self.__wydzial

    @wydzial.setter
    def wydzial(self, value):
        pass
    
    @property
    def kierunek(self):
        return self.__kierunek
    
    @kierunek.setter
    def kierunek(self, value):
        pass
    
    @property
    def nr_indeks(self):
        return self.__nr_indeks
    
    @nr_indeks.setter
    def nr_indeks(self, value):
        pass