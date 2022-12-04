def demo_print():
    '''
    how demo print works
    :return: void
    '''
    print('mo4km', 'm')
    print('mo4km', 'm', sep='; ')
    print('mo4km', 'm', sep='; ', end='.\n')
    imiona = ["Kamil", "Darek", "Jacek"]

    print(*imiona, sep=', ')
    long_text = """
this is multi line text 
    with tab
or without tab
"""
    print(long_text)
    first_name = "Kamil"
    last_name = "K"
    print("{0} {1}".format(first_name, last_name))
    print(f"{first_name} {last_name}")

    # how to open or save file
    with open(r"files\names.txt", "a", encoding="utf-8") as name_file:
        print(*imiona, sep=";", file=name_file)

    liczba = 4567.789123
    print(f"{liczba:.2f}")
    cls()