"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""
def my_sum(a:float, b:float, c:float) ->float:
    list_1 = [a, b, c]
    d = max(list_1)
    list_1.remove(d)
    e = max(list_1)
    res = d + e
    return res
print(my_sum(1, 10, 2))