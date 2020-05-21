"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""
def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname='Ivanov', name='Ivan', year='1977', city='Msk', email='2@mail.ru',telephone='8-800-555-35-35'))