import functools
import math

from lib.utils.utils_validators import isnumber


def circle_field(radius: float):
    return math.pi * math.pow(radius, 2)


# circumference of a circle
def circumference_circle(radius: float):
    return 2 * math.pi * radius


# Rectangle field
def rectangle_field(a: float, b: float = 0):
    if b == 0: return a ** 2
    return a * b


# cylinder field
def cylinder_field(radius: float, height: float):
    return (2 * circle_field(radius)) + (rectangle_field(height, circumference_circle(radius)))


# cylinder volume
def cylinder_volume(radius: float, height: float):
    return circle_field(radius) * height


def circle(radius: float, **what_count):
    """
    Function count field or circumference of a circle.
    :param radius: float
    :param what_count: 'field' or 'circumference', example: count='field'
    :return:
    """
    if what_count.get('count').lower() == 'field':
        return circle_field(radius)
    elif what_count.get('count').lower() == 'circumference':
        return circumference_circle(radius)
    else:
        raise AttributeError('You need to specify count as field or circumference.')


def quadratic_equation(a: float, b: float, c: float):
    """
    This function counts quadratic equation.
    :param a:
    :param b:
    :param c:
    :return:
    """
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return "no solutions"
    elif delta == 0:
        return -b / (2 * a)
    else:
        return (
            (-b - math.sqrt(delta) / (2 * a)),
            (-b + math.sqrt(delta) / (2 * a))
        )


def sum_recursively(*data):
    suma = 0.
    for v in data:
        if isinstance(v, (int, float)):
            suma = +v
        if isinstance(v, str):
            if isnumber(v):
                suma += float(v)
        if isinstance(v, (list, tuple, set, frozenset)):
            for w in v:
                suma += sum_recursively(w)
    return suma


def is_number_even(value: int):
    if value % 2 == 0:
        return True
    else:
        return False


# extra challenge
# function doubles number from argument

def double(value):
    if isinstance(value, str):
        if isnumber(value): value = float(value)
    return value * 2

#dekorator do cachowania ¿eby funkcje rekurencyjne wykonywa³y siê szybciej
@functools.lru_cache()
def fib(n):
    if n <= 2:
        wynik = n
    else:
        wynik = fib(n - 1) + fib(n - 2)
    return wynik
