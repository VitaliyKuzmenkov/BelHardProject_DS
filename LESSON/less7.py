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
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data - Лист1.csv')

x = [float(elem.replace(',', '.')) for elem in df['X']]

y = [float(elem.replace(',', '.')) for elem in df['Y']]

plt.plot(x, y)
plt.xlabel('Название оси X')
plt.ylabel('Название оси Y')
plt.title('Название графика')
plt.show()

""""Кривая доходности" в финансах - это график, показывающий доходность 
или процентные ставки в зависимости от длины контракта (2 месяца, 2 года, 20 лет и т.д.). 
Проценты в долларах, выплачиваемые по ценным бумагам казначейства США 
(U.S. Treasury securities) для разных сроков погашения, представляют интерес для трейдеров, 
и такой график неформально называют "the yield curve" - кривая доходности."""


labels = ['1 Mo', '3 Mo', '6 Mo', '1 Yr', '2 Yr', '3 Yr', '5 Yr', '7 Yr', '10 Yr', '20 Yr', '30 Yr']
july16_2007 =[4.75,4.98,5.08,5.01,4.89,4.89,4.95,4.99,5.05,5.21,5.14]
july16_2020 = [0.12,0.11,0.13,0.14,0.16,0.17,0.28,0.46,0.62,1.09,1.31]