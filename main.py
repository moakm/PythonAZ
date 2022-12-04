from challenges.day01 import c01_BMI, c02_matma
from challenges.day02 import import_web_api_random_people, countries_search_engine_by_continent, numbers_tests
from challenges.day04 import c06_classes
from demos.demo01_print import demo_print
from demos.demo02_datatypes import demo_datatypes
from demos.demo03_struktury import demo_struktury
from demos.demo04_texts import demo_texts
from demos.demo05_collections import demo_collections
from demos.demo06_webAPI import import_web_api_nbp
from demos.demo07_custom_functions import demo_custom_functions
from demos.demo08_files import demo_files
from demos.demo09_db import demo_sqlite
from demos.demo10_oop import demo_oop
from demos.demo11_gui import demo_gui
import sys

from demos.demo12_spec_func import demo_spec_func

# Pass an argument
#arg1 = sys.argv[1]

while True:
    print("Choose operation: ")
    print("1- demo print")
    print("2 - demo data types")
    print("3 - demo structures")
    print("4 - demo texts")
    print("5 - demo collections")
    print("6 - demo Web API")
    print("7 - demo custom functions")
    print("8 - demo files handling")
    print("9 - demo SQL")
    print("10 - demo OOP")
    print("11 - demo GUI PyQt6")
    print("12 - demo special funcions")
    print("c1 - challenge 1")
    print("c2 - challenge 2 mata")
    print("c3 - challenge 3 web api")
    print("c4 - challenge 4 web api region search engine")
    print("c5 - challenge 5 numbers tests")
    print("c6 - challenge 6 classes")
    print("anything to quit")
    user_input = input()

    if user_input == "1":
        demo_print()
    elif user_input == "2":
        demo_datatypes()
    elif user_input == "3":
        demo_struktury()
    elif user_input == "4":
        demo_texts()
    elif user_input == "5":
        demo_collections()
    elif user_input == "6":
        import_web_api_nbp()
    elif user_input == "7":
        demo_custom_functions()
    elif user_input == "8":
        demo_files()
    elif user_input == "9":
        demo_sqlite()
    elif user_input == "10":
        demo_oop()
    elif user_input == "11":
        demo_gui()
    elif user_input == "12":
        demo_spec_func()
    elif user_input == "c1":
        c01_BMI()
    elif user_input == "c2":
        c02_matma()
    elif user_input == "c3":
        import_web_api_random_people()
    elif user_input == "c4":
        countries_search_engine_by_continent()
    elif user_input == "c5":
        numbers_tests()
    elif user_input == "c6":
        c06_classes()
    else:
        print("Bye...")
        break
