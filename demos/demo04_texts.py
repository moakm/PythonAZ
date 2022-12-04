from lib.utils.utils_validators import isnumber, is_pesel_valid
from lib.utils.util_console_mgmt import cls

def demo_texts():
    # text1 = "We are learning python today"
    # print(text1.upper())
    # print(text1.lower())
    # print(text1.title())
    # print(text1.capitalize())
    #
    pesel = "09090912345"
    # if pesel.isdigit(): print("only digits")
    # print(len(pesel))
    # print("123.45".isdigit())
    # print("123.45".isnumeric())
    # print("123.45".isdecimal())
    # print(isnumber("123.45"))
    #
    # print(text1[:15])
    # print(text1[16:])
    #
    # text2 = "   some text     "
    # print(len(text2))
    # text2 = text2.strip()
    # print(len(text2))
    #
    # person = "Kamil Kopczynski"
    # print(person[:person.find(" ")])
    # print(person[person.find(" ")+1:])

    try:
        if is_pesel_valid(pesel):
            print("pesel ok")
    except:
        print("error")


    cls()