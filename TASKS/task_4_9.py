import random

"""Создать матрицу, найти максимальное значение матрицы."""

"""Первый способ"""

matrix = [[random.randint(-10, 10) for i in range(3)] for j in range(3)]

print(matrix)
print(max(map(max, matrix)))

"""Второй способ"""

max_elem = 0
for i in range(3):
    for j in range(3):
        if matrix[i][j] > max_elem:
            max_elem = matrix[i][j]
print(max_elem)
