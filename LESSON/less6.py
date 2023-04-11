# """Реализуйте механизм сложения векторов.
# Есть 2 вектора в результате работы программы нужно
# вернуть вектор каждая координата которого является
# суммой координаты 2 векторов.
# """
#
# length_vector_1 = input("размер вектора 1: ")
# length_vector_2 = input("размер вектора 2: ")
#
# try:
#     if not int(length_vector_1) == int(length_vector_2):
#         raise ValueError('Длинны векторов дожны быть одинаковыми')
#
# except:
#     raise ValueError('Длинны векторов дожны быть одинаковыми')
# try:
#
#     a, b, c, d, e, f = float(input('a: ')), float(input('b: ')), float(input('c: ')), float(input('d: ')), float(input('e: ')), float(input('f: '))
#
# except:
#     print("Некорректные значения для координаты времени")
#
# d_1 = {
#     "x": a,
#     "y": b,
#     "z": c,
#     }
# d_2 = {
#     "x": d,
#     "y": e,
#     "z": f,
#     }
#
# res = []
#
# for key, value in d_1.items():
#
#     v = value + d_2.get(key)
#     res.append(v)
#
# print(res)

"""Есть матрица A размерностью 3*3 (список списков), напишите программу,
которая создает транспонированную матрицу.
"""

import numpy as np
a = np.array([[0, 1, 2], [4, 5, 6], [7, 8, 9]])
b = a.transpose()
c = a.dot(b)
print(a)
print(b)
print(c)



# A = [[5, 4, 3], [2, 4, 6], [4, 7, 9], [8, 1, 3]]
# traspon_A = []
# print(A)
# for a in range(len(A)):
#     for b in range(len(A[0])):
#         traspon_A[b][a] = A[a][b]
# print(A)

# m = [[0, 1, 2], [4, 5, 6], [7, 8, 9]]
# for row in m:
#     print(row)
# rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
# print("\n")
# for row in rez:
#     print(row)