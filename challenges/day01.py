from lib.utils.util_person import calculateBMI, ratingBMI
from lib.matma.util_matma import circle_field, circumference_circle, \
    rectangle_field, cylinder_field, cylinder_volume
from lib.utils.util_console_mgmt import cls


# challenge 1 write function to calculate BMI
def c01_BMI():
    w = float(input("Your weight [kg]: "))
    h = float(input("Your height [m]: "))
    result = calculateBMI(h, w)
    print( f"BMI = {result:.2f} -> {ratingBMI(result)}")
    cls()

# challenge 02 math
def c02_matma():
    r = 4.
    h = 8.3
    a = 6.
    b = 9.
    print(f"Circle field = {circle_field(r):.2f}")
    print(f"circumference of a circle = {circumference_circle(r):.2f}")
    print(f"rectangle field = {rectangle_field(a, b):.2f}")
    print(f"cylinder field = {cylinder_field(r, h):.2f}")
    print(f"cylinder volume = {cylinder_volume(r, h):.2f}")
    cls()