#exercise 1
a = 10
b = 15
print("Переменные a и b - ", a, b)
string1 = input("Введите первую строку ")
number1 = (input("Введите первое число "))
string2 = input("Введите вторую строку ")
number2 = int(input("Введите второе число "))
print("Введеные значения - %10s %5d %10s %5d" % (string1, number1, string2, number2))
#exercise 2
second = (input('введите время в секундах\n'))
hour = 0
minute = 0
if second.isdigit():
    second = int(second)
    while second >= 3600:
        hour += 1
        second -= 3600
    else:
        while second >= 60:
            minute += 1
            second -= 60
            print(f"Время в формате чч:мм:сс   {hour} : {minute} : {second}")
else:
    print('Введите время!')

#exercise 3
number = (input('Введите число n\n'))
if number.isdigit():
    number2 = number + number
    number3 = number + number2
    result = int(number2) + int(number3) + int(number)
    print('сумма n+nn+nnn=', result)
else:
    print('Введите число цифрой')

#exercise 4
num = input('Введите число,мы найдем наибольшую цифру \n')
if num.isdigit():
    num = int(num)
    big = num % 10
    num = num // 10
    while num // 10 >= 0:
        if num % 10 > big:
            big = num % 10
        else:
            print(big)
            break
else:
    print("введите цифру")
#exerciese 5
money = input('Введите выручку \n')
expense = input('Введите издержки \n')
if money.isdigit() and expense.isdigit():
    money = int(money)
    expense = int(expense)
    if money > expense:
        print('Выручка привышает издержки')
        print('Рентабельность =' , money / expense)
        emp = input('Введите число работников \n')
        if emp.isdigit():
            emp = int(emp)
            print("Прибыль на человека=", emp / (money - expense))
        else:
            print('Введите число работников')
    elif money < expense:
        print("Издержки привышают выручку")
    else:
        print("Вы в нуле")
else:
    print("Введите Числом")
#exerciese 6
first_day = 5
days_lost = 1
expectation = 70
print(first_day)
while float(expectation) > float(first_day):
    first_day = first_day + first_day * 0.1
    days_lost += 1
print('Чтобы пробежать',expectation, 'километров, нужно бегать',days_lost,'дней')
