def isnumber(value):
    try:
        digit = float(value)
        return True
    except:
        return False


def is_pesel_valid(pesel: str):
    if len(pesel) == 11:
        if pesel.isdigit():
            month = int(pesel[2:4])
            if month in range(1, 13) or month in range(21, 33):
                dzien = int(pesel[4:6])
                if dzien in range(1, 32):
                    return True
            else:
                return False
    else:
        return False

def oznaczenia_projektow(p):
    for i in range(1, p):
        yield f"projekt nr {i}"