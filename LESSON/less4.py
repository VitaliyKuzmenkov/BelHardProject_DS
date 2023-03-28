# age = 25
#
# print(age > 5)


# lst = [1,22,3,4,5]
# if lst:
#     print(lst)
# else:
#     print("list empty")

# n = int(input())
#
# data = [1, 2, 3, 4, 5, 6]
#
# res = [elem * n for elem in data] if n % 2 == 0 else data * int(n)
#
# print(res)

# season = int(input("Введите пару года  "))
#
# seasons = {
#     1: 'Зима',
#     2: 'Весна',
#     3: 'Лето',
#     4: 'Осень'
# }
#
# print(seasons.get(season))


# lst = [1 , 2, 3, 4, 5, 6, 7, 8, 9]
# summ = 0
# counter = 0
# for i in lst:
#     summ += i
#     counter += 1
#     print(i)
#     if summ == 15:
#         print(summ)
#         print(counter)
#         break

# str1 = "Break and Continue operstors"
#
# for index, i in enumerate(str1):
#     if index % 3 == 0 and index != 0:
#         continue
#     print(i, end='')
#     if i == 'p':
#         break

# lst = ['snow', 'rain', 'wind', 'sun', 'clouds']
# for i in lst:
#     for index, j in enumerate(i):
#         if index > 2:
#             print(i)

# username = input("Введите имя пользователя: ")
# password = input("Введите пароль: ")
#
# while len(password) < 8 or username in password:
#     print("Не подходит под условие")
#     password = input("Введите пароль: ")
#
# print("Пароль принят.")


def summ(a, b):
    summ = a + b
    return summ


def raz(a, b):
    raz = a - b
    return raz


def de(a, b):
    de = a / b
    return de


def ymn(a, b):
    ymn = a * b
    return ymn


a = int(input("Введите 1-ое число -  "))
b = int(input("Введите 2-ое число -  "))
z = input("Введите знак -  ")

zz = {
    "+": summ(a, b),
    '-': raz(a, b),
    '/': de(a, b),
    '*': ymn(a, b)
}

print(zz.get(z))

# first_number = int(input('Первое число: '))
# sign = input('Введите знак: ')
# second_number = int(input('Второе число: '))
#
# if sign == '+':
#     print(first_number + second_number)
#
# if sign == '-':
#     print(first_number - second_number)
#
# if sign == '*':
#     print(first_number * second_number)
#
# if sign == '/':
#     print(first_number / second_number)
