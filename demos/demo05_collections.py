from lib.utils.util_console_mgmt import cls
import locale


def demo_collections():
    locale.setlocale(locale.LC_ALL, "pl-PL")
    surnames=["Majewski", "Ziółkiewski", "Żurek"]
    surnames.sort(key=locale.strxfrm)
    # [print(value) for value in surnames]
    surnames.append("Brzęczek")
    surnames.insert(2, "Źrebak")

    # dict (json -javascript object notation)

    person = {
        "name": "Kamil",
        "surname": "Kopczynski",
        "age": 28,
        "certs": ["AD cert", "Python developer"],
        "kids": [
            {
                "name": "Ami",
                "surname": "Kopczynska",
                "age": 3,
            },
            {
                "name": "Kacper",
                "surname": "Kopczynski",
                "age": 1,
            }]
    }
    print(person.get("kids")[0].get("name"))
    # insert key value pair
    person["city"] = "Rybnik"
    # [print(keys) for keys in person.keys()] # only keys
    # [print(values) for values in person.values()] # only values
    [print(f"{k} : {v}") for k, v in person.items()]  # items contains keys and values
    # remove data from dict
    del person["city"]
    [print(f"{k} : {v}") for k, v in person.items()]  # items contains keys and values

    cls()
