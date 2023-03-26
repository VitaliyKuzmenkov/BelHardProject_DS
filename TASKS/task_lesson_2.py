"""Дан список из 10 элементов. Удалить все элементы,
расположенные перед минимальным элементом списка."""

import random

lst = [random.randint(1, 100) for i in range(10)]

print(lst)

min_el = min(lst)
ind_el = lst.index(min_el)
del lst[:ind_el]
print(lst)