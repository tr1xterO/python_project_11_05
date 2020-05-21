"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""
def my_f(a:float, b:float) -> float:
    while True:
        try:
            res = a / b
            break
        except ValueError as error:
            print("Вы ввели не числа")
            continue
        except ZeroDivisionError:
            res = 0
            continue
    return res
print(my_f(5, 6))