class ArgumentIsNotIntegerError(Exception):
    """Выбрасывается, когда аргумент не целое число!"""
    pass

def summa(a, b):
    return a + b


def difference(c, d):
    return c - d


def division(e, f):
    if f == 0:
        raise ZeroDivisionError("Делить на ноль нельзя")
    return e / f


def multiplication(g, i):
    return g * i


try:
    a = int(input("Введите 1-ое число -  "))
    sign = input("Введите знак -  ")
    b = int(input("Введите 2-ое число -  "))

    sign_calculator = {
        "+": summa(a, b),
        '-': difference(a, b),
        '/': division(a, b),
        '*': multiplication(a, b)
    }

    print(sign_calculator.get(sign))
except ArgumentIsNotIntegerError("Аргументы должны быть целыми числами") as exc:
    print(exc)
