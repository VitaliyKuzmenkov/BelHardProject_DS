"""Создайте текстовый файл.
Запишите в него 10 рандомных значений. После прочтите этот файл,
определите все возможные комбинации и запишите их в другой файл.
Для нового файла вычислите медиану и среднее значение.
"""

from random import randint
import itertools

with open('task_5_3_1.txt', 'w') as file:
    data_num = [randint(0, 10) for i in range(10)]
    file.write(str(data_num))
    data_comb = list(itertools.combinations(data_num, 2))
    data_str = str(data_comb)
    print(data_str)
    with open('task_5_3_1new.txt', 'w') as file_new:
        file_new.write(data_str)

