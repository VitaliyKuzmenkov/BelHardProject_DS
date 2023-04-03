import pandas as pd
import csv, os
"""Запросить у пользователя данные (имя, фамилия, возраст) 
и создать файл с этими значениями"""

with open('info.txt', 'a+') as file:
    name = input("Введите имя - ")
    surname = input("Введите фамилию - ")
    age = input("Введите возраст - ")
    file.write(name)
    file.write(' ')
    file.write(surname)
    file.write(' ')
    file.write(age)

