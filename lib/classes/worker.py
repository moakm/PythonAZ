from lib.classes.person import Person


class Worker(Person):
    __structure = {
        "HR": ["kadrowa", "wredna kadrowa"],
        "IT": ["administrator sieci", "programista", "administrator systemów", "specjalista IT"],
        "MGM": ["prezes", "v-ce prezes", "kierownik", "właściciel"],
        "PROD": ["specjalista", "magazynier", "operator", "mistrz zmiany"]
    }
    __department = ""
    __job = ""
    __salary = 0.0

    def __str__(self):
        return (f"{super().__str__()}, pracuje w dziale {self.department} "
                f"na stanowisku {self.job}")

    def __init__(self, fname: str, lname: str, pesel: str, department: str, position: str, salary: float):
        super().__init__(fname, lname)  # użycie klasy bazowej
        self.pesel = pesel
        self.department = department
        self.job = position
        self.salary = salary

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        if value in self.__structure.keys():
            self.__department = value
        else:
            raise AttributeError("Deprtment not found")

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, value):
        if value in self.__structure.get(self.department):
            self.__job = value
        else:
            raise AttributeError(f"Position not found in {self.department}")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        pass

    @classmethod
    def get_company_structure(cls):
        return cls.__structure
