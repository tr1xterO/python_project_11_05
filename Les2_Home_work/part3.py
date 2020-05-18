'''Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.'''
# Реализация через list
lis1 = [12,1,2]
lis2 = [3,4,5]
lis3 = [6,7,8]
lis4 = [9,10,11]
number = input('введите № месяца\n',)
if number.isdigit():
    number = int(number)
    if number in lis1:
        print('Это зима')
    elif number in lis2:
        print('Это весна')
    elif number in lis3:
        print('Это лето')
    elif number in lis4:
        print('Это осень')
    else:
        print("В году 12 месяцев")
else:
    print("Введите числом")

# Реализаця через dict
mon = {'1': "Зима", '2': 'Зима', '3': 'Весна', '4': 'Весна', '5': "Весна", '6': 'Лето', '7': 'Лето', '8': 'Лето', '9': 'Осень', '10': 'Осень', '11': 'Осень', '12': 'Зима', }
number1 = input('введите № месяца\n',)
if number1.isdigit():
    if number1 in mon:
        print(mon[number1])
    else:
        print('В году 12 месяцев')
else:
    print("введите число")