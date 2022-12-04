import math


def gender(pesel: str):
    if int(pesel[9]) % 2 == 0:
        return "W"
    else:
        return "M"


def birth_date(pesel: str):
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if month > 12 and month <= 32:
        month -= 20
        year += 2000
    elif month > 80:
        month -= 80
        year += 1800
    else:
        year += 1900
    import datetime
    return (datetime.date(year, month, day))


def calculateBMI(height: float, weight: float):
    bmi = weight / math.pow(height, 2)
    return bmi


def ratingBMI(resultBMI: float):
    if resultBMI < 16.0:
        return "wygłodzenie"
    elif 16.0 < resultBMI < 16.99:
        return "wychudzenie"
    elif 17.0 < resultBMI < 18.49:
        return "niedowaga"
    elif 18.5 < resultBMI < 24.99:
        return "pożądana masa ciała"
    elif 25.0 < resultBMI < 29.99:
        return "nadwaga"
    elif 30.0 < resultBMI < 34.99:
        return "otyłość 1 st"
    elif 35.0 < resultBMI < 39.99:
        return "otyłość 2 st"
    elif resultBMI >= 40:
        return "otyłość 3 st"


def kids_list(*kids):
    kids = list(kids)
    kids.sort()
    print("Kids on party: ")
    for i, k in enumerate(kids, start=1):
        print(f"{i}. {k}")
