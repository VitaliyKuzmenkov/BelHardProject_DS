import random

"""Создать матрицу 3*3, заполнить ее рандомными значениями. 
Заменить все четные числа на нули"""

matrix = [[random.randint(-10, 10) for i in range(3)] for j in range(3)]

print(matrix)

for i in range(3):
    for j in range(3):
        if matrix[i][j] % 2 == 0:
            matrix[i][j] = 0
print(matrix)
