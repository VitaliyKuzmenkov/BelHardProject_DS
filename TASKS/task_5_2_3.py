"""Напишите программу, которая будет открывать определенный файл file
 и выводить на печать построчно последние строки в количестве lines
 (на всякий случай проверим, что задано положительное целое число).
"""
with open('info.txt', 'r', encoding='utf-8') as text_file:
    file = [i.strip('\n') for i in text_file]
    print(file)


def read_last(lines, file):
    return file[-lines:]


while True:
    try:
        lines = int(input('Введите количество строк: '))
        if lines <= 0:
            raise TypeError
        break
    except ValueError:
        print('Введи число!')
    except TypeError:
        print('Количество cтрок не может быть ноль или менее нуля.')

print(read_last(lines=lines, file=file))
