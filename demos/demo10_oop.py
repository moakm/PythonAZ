from lib.classes.student import Student
from lib.classes.studia import Studia
from lib.utils.util_console_mgmt import cls


def demo_oop():
    from lib.classes.person import Person
    from lib.classes.worker import Worker

    try:
        person1 = Person(
            "Adam", "Niezgodka"
        )
        print(f"{person1.first_name} {person1.get_last_name()}")
        person1.first_name = 'Jan'
        person1.set_last_name('Kowalski')
        person1.pesel = '12121212351'

        print(person1)

        for d in Worker.get_company_structure().keys():
            print(f"{d}: ")
            for s in Worker.get_company_structure().get(d):
                print(f"\t{s}")

        worker1 = Worker("Ania", "Nowak", "01123112345", "IT", "programista", 1234)
        print(worker1)
        print(Worker.bmi(80.4, 1.7))

        uczelnia = Studia("elektronika", "automatyka", "asd1234")
        student1 = Student(person1, uczelnia)
        print(student1)

    except AttributeError as e:
        print(e)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Always run closing code.")

    # print(Person.bmi(80.4, 1.7))
    cls()
