"""Напишите программу, в которой пользователь вводит целое число
а программа каждую цифру в этом числе меняет на «дополнение до 9,
цифра 0 меняется на 9, цифра 1 меняется на 8, цифра 2 меняется на 7
и так далее - цифра 8 меняется на 1, а цифра 9 меняется на 0.
"""

num = input("Введите целое число -- ")
lst_new = []
for i in num:
    lst_new.insert(0, (9 - int(i)))
lst_new = lst_new[::-1]
num_new = int(''.join(map(str, lst_new)))

print(num_new)


