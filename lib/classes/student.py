from lib.classes.person import Person
from lib.classes.studia import Studia


class Student(Person, Studia):
    def __init__(self, person, student):
        Person.__init__(self, person.first_name, person.get_last_name())
        self.pesel = person.pesel
        Studia.__init__(self, student.wydzial, student.kierunek, student.nr_indeks)

    def __str__(self):
        return f"{Person.__str__(self)} {Studia.__str__(self)}"