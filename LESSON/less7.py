# import numpy as np
#
# python_list = [1, 2, 3, 4, 5, 6]
# numpy_array = np.array(python_list)
#
# message = f"Список {python_list} имеет тип данных - {type(python_list)}, а созданный \n на его основе массив numpy: {numpy_array} имеет тип {type(numpy_array)}"
#
# print(message)
#
# import numpy as np
#
# flat_array = np.arange(5)
#
# test_arr = np.arange(1, 10)
#
# param_arr = np.arange(1, 1000, 50)
#
# print(f"flat_array \n{flat_array}\n test_arr: \n{test_arr}\n param_arr \n{param_arr}")
# import itertools
#
# lst = ['red', 'green', 'white', 'black']
# for i in itertools.combinations(lst, 3):
#     print(' '.join(i))
# print()
# for i in itertools.permutations(lst, 3):
#     print(' '.join(i))
"""Как такое может быть? Все дело в том, что если известно,
что как минимум один ребенок - девочка, то вероятность,
что в семье имеется один мальчик и одна девочка,
в два раза выше, чем вероятность, что имеются две девочки
Можно убедиться в правильности рассуждений,
"сгенерировав" большое количество семей:
Задача
C помощью модуля random реализуйте выбор между мальчиком и девочкой.
Провести эксперимент на совокупности из 10000 семей
"""
# from random import randint
# import numpy as np
# older_girl = 0
# both_girl = 0
# kind_girl = 0
# family = [randint(0, 2) for i in range(1)]
# for i in family:
#     if i == 0:
#         older_girl += 1
#     if i == 1:
#         both_girl += 1
#     if i == 2:
#         kind_girl += 1
# print(family)
# print(older_girl/3*100)
# print(both_girl/3*100)
# print(kind_girl/3*100)
