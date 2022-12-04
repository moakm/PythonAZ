import time

from lib.matma.util_matma import fib
from lib.utils.util_console_mgmt import cls
from lib.utils.utils_validators import oznaczenia_projektow


def demo_spec_func():
    directors = ["Akira Kurosawa", "Tim Burton", "Quentin Tarantino", "Papryk Wega"]
    movies = ["7 samurajów", "9", "Pulp fiction", "Kobiety mafii"]

    for i, (d, m) in enumerate(zip(directors, movies), start=1):
        print(f"{i}. Movie {m} directed by {d}")

    liczby = [12, 34, 54, 31, 34]
    from lib.matma.util_matma import circumference_circle
    obwody = list(map(circumference_circle, liczby))
    for o in obwody:
        print(o)

    from lib.matma.util_matma import is_number_even
    parzyste = list(filter(is_number_even, liczby))
    for n in parzyste:
        print(n)

    print("-*-" * 10)

    nieparzyste = list(filter(lambda x: x % 2 == 1, liczby))
    for l in nieparzyste:
        print(l)

    liczba = 8
    kod_eval = "100 * 200 * 300 * liczba"
    kode_exec = """
linia = 34
linia += 37
    """
    # start = time.time()
    # for i in range(1000000):
    #     eval(kod_eval)
    #     exec(kode_exec)
    # print(f"Operation time {time.time()-start}")

    start = time.time()
    kod_comp_eval = compile(kod_eval, "comment", 'eval')
    kod_comp_exec = compile(kode_exec, "comment", 'exec')
    for i in range(1000000):
        eval(kod_comp_eval)
        exec(kod_comp_exec)
    print(f"Operation time {time.time() - start}")

    start = time.time()
    for i in range(10):
        print(f"{i} -> {fib(i)} - czas : {time.time() - start}")

    try:
        gen_proj = oznaczenia_projektow(5)
        print(next(gen_proj))
        print(next(gen_proj))
        print(next(gen_proj))
        print(next(gen_proj))
        print(next(gen_proj))
        print(next(gen_proj))
        print(next(gen_proj))
        print(next(gen_proj))
    except Exception as e:
        print(e)

    try:
        gen_director = iter(directors)
        print(next(gen_director))
        print(next(gen_director))
        print(next(gen_director))
        print(next(gen_director))
        print(next(gen_director))
        print(next(gen_director))
        print(next(gen_director))
        print(next(gen_director))
    except Exception as e:
        print(e)

    def webscrapping():
        from bs4 import BeautifulSoup as bs
        import requests

        url = "https://www.worldometers.info/coronavirus/"
        dane = requests.get(url)
        zupa = bs(dane.text, 'html.parser')
        dane_corona = zupa.findAll("div", class_="maincounter-number")
        all = dane_corona[0].text.replace(',', ' ').strip('\n').strip(' ')
        death = dane_corona[1].text.replace(',', ' ').strip('\n')
        cured = dane_corona[2].text.replace(',', ' ').strip('\n')
        print(f"Zachorowalo : {all},\n"
              f"zmarlo: {death},\n"
              f"Wyleczeni: {cured}")

    webscrapping()

    cls()
