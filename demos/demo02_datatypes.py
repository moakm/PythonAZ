from lib.utils.util_console_mgmt import cls


def demo_datatypes():
    #primitive types
    a = "mo4km"
    print(a, type(a))
    b = 32
    print(b, type(b))
    c = 5.4
    print(c, type(c))
    d = True
    print(d, type(d))

    #complex types
    e = 4 + 5.5j
    print(e, type(e))

    import datetime
    f = datetime.datetime.now()
    print(f, type(f))

    import math
    g = math.pi
    print(g, type(g))

    #collections
    my_list = ["mo4km", 94, 22.23, [1, "andrzej"]]
    my_list.append("Warzecha")
    print(*my_list)

    #static tuple, not able to modify
    my_tuple = (21, 94.2, "mo4km")
    print(my_tuple)

    #set is dynamic collection without doubles.
    my_set = {12, 32, 56, 12, 2}

    my_frozenset = frozenset(my_set)

    #dictionary or map type
    person = {
        "first name": "kamil",
        "last name": "kopczyński",
        "age": 28,
        "certs":["AD cert", "Python dev"]
    }
    print(*person.get("certs"), sep=", ")
    cls()