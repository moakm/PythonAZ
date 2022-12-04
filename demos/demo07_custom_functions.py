from lib.matma.util_matma import rectangle_field, circle, quadratic_equation, sum_recursively
from lib.utils.util_console_mgmt import cls
from lib.utils.util_person import kids_list


def demo_custom_functions():
    a = 3.5
    b = 6.7
    print(rectangle_field(a))
    print(rectangle_field(a, b))

    kids_list("Jacek", "Kamila", "Borys", "Szymon")
    kids_list("Jacek", "Kamila", "Kamil", "Borys", "Szymon", "Darek")

    print(circle.__doc__)
    print(f"Circle field: {circle(4.5, count='field'):.2f}")
    print(f"Circle circumference: {circle(4.5, count='circumference'):.2f}")

    result = quadratic_equation(1, 3, 1)
    if isinstance(result, str):
        print(result)
    elif isinstance(result, float):
        print(f"{result:.2f}")
    else:
        print(f"x1= {result[0]:.2f}, x2= {result[1]:.2f}")

    result = sum_recursively(123, 345.67, "123.5")
    print(f"{result:.2f}")
    result = sum_recursively([123, 45.6, 12], (56.45, 12), {321, 98.8})
    print(f"{result:.2f}")

    cls()
