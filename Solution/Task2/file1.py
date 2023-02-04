
class Error(Exception):
    """Base class for other exceptions"""
    pass

class TwoDivisionError (Error):
    """Не может делиться на 2"""
    pass

class ValueProblem(Error):
    """не входит в диапозон данных"""
    pass
try:
    a = int(input("Введите числитель:"))
    if (a >= 5) & (a <= 7):
        raise ValueProblem ("Нельзя использовать числа в интервале от 5 до 7")
    b = int(input("Введите знаменатель:"))
    if b==2:
        raise TwoDivisionError("Нельзя использовать 2")
        print()
    print(a/b)
except TwoDivisionError as err:
    print(str(err))
except ValueProblem as erg:
    print(str(erg))
finally:
    print("Прошла проверку")