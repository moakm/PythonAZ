import math

from lib.utils.util_console_mgmt import cls
from lib.utils.util_person import gender, birth_date


def demo_struktury():
    # iterations
    for i in range(3, 16): print(i, end=", ")

    for i in range(3, 17, 3): print(i, end=", ")
    print("")

    people = ["Darek", "Jacek", "Kamila", "Andrzej", "Anna"]
    for value in people:
        print(value)

    print("List of invited guests ")
    for n, person in enumerate(people, start=1): print(f"{n}. {person}")
    print("-*-" * 8)
    # one line code
    [print(f"{n}. {person}") for n, person in enumerate(people, start=1)]
    print("-*-" * 8)
    for person in people:
        if person == "Anna":
            print("There is Anna")
            break
    else:
        print("Anna is not on the list")
    print("-*-" * 8)
    n = 0
    while n < 15:
        print(n)
        n += 1
    print("-*-" * 8)
    entities = len(people)
    while i < entities:
        if people[i] == "anna":
            print("Anna is on the list")
            i += 1
    else:
        print("Anna is not on the list")

    pesele = ["75120312345", "85090123456", "01271834567", "06251479291"]
    [print(f"{value} -> {gender(value)}, {birth_date(value)}") for value in pesele]
    cls()

    cls()
