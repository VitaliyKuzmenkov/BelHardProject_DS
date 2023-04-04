"""Создайте текстовый файл.
Запишите в него 10 рандомных значений. После прочтите этот файл,
определите все возможные комбинации и запишите их в другой файл.
Для нового файла вычислите медиану и среднее значение.
"""

from random import randint
import csv
import pandas as pd

with open('task_5_3_1.txt', 'w+') as txtfile:
    data_num = str([randint(0, 10) for i in range(15)])
    txtfile.write(data_num)

with open('task_5_3_1.csv', 'w+') as csvfile:
    df = pd.read_csv('task_5_3_1.txt', sep=',')
    df.to_csv('task_5_3_1.csv')

    print('DataFrame\n----------')
    print(df)
    mean = df.mean()
    print('\nMean\n------')
    print(mean)
    median = df.median ()
    print('\n Median \n------')
    print(median)

