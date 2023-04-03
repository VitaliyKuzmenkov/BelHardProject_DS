import pandas as pd
import csv, os

"""Создать и прочитать CSV файл с помощью Pandas"""

with open('automobile.csv', 'w+') as csvfile:

    columns = ['Date', 'Model', 'Mark']
    data = [
        ['2023-04-04', 'BMW', 'IX'],
        ['2023-04-04', 'AUDI', 'e-tron'],
        ['2023-04-04', 'Tesla', 'Model X'],
        ['2023-04-04', 'Mercedes', 'EQC']
    ]
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(r'automobile.csv')
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
