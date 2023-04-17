# import random
#
#
# def cat_voice():
#     return ('Meow!')
#
#
# def dog_voice():
#     return ('Woof!')
#
#
# print(dog_voice())
# print(cat_voice())
#
#
# def get_voice(text):
#     return (f'Hello, {text} !')
#
#
# print(get_voice('Vitaliy'))
#
#
# def gen(a,b,c):
#     num = []
#     for i in range(c):
#         num_elem = random.randint(a, b)
#         if num_elem % 2 == 0:
#             num.append(num_elem)
#     return num
#
#
# print(gen(1,9,10))
#
#
# def gen_1(a,b):
#     num = []
#     num = [i for i in range(a, b) if i % 2 == 0]
#     return num
#
#
# print(gen_1(1,9))
#
#
# name_gef = lambda name: f"Hello {name} !"
#
# print(name_gef("efjf"))
#
# data = ["ndvkldnsvkdj", "kdbwbhdkh"]
# res = list(map(len, data))
# print(res)


#
# """Создайте функцию is_cat_here(), которая принимает
# любое количество аргументов и проверяет есть ли строка 'cat' среди них.
# Функция должна возвращать True, если такой параметр есть и False в обратном случае.
# Буквы в строке 'cat' могут быть как большие, так и маленькие.
# """
#
#
# def is_cat_here(*args):
#     for elem in args:
#         if elem == "cat":
#             return True
#         else:
#             return False
#
#
# print(is_cat_here(5, "cat", 5))
#
# """Создайте функцию is_item_here(item, *args),
# которая проверяет есть ли  item среди args.
# Функция должна возвращать True, если такой параметр есть и False в обратном случае.
# """
#
# def is_item_here(item, *args):
#     return item in args
#
# print(is_item_here(1, "ekqf"))
#
#
# """Создайте функцию your_favorite_color() с позиционным параметром my_color и параметрами **kwargs,
# которая будет выводить на экран 'My favorite color is (значение my_color),
# what is your favorite color?', если в параметрах kwargs нет ключа color,
# и 'My favorite color is (значение my_color), but (значение по ключу color)
# is also pretty good!', если в параметрах kwargs ключ color присутствует"""
#
# def your_favorite_color(my_color, **kwargs):
#     if kwargs.get("color") is None:
#         return f'My favorite color is {my_color}, what is your favorite color?'
#     return f'My favorite color is {my_color}, but (значение по ключу color) is also pretty good!'
#
# print(your_favorite_color("red"))

def kva_yr(*args):
    a = int(input('Введите значение a = '))
    b = int(input('Введите значение b = '))
    c = int(input('Введите значение c = '))

    if a == 0:
        raise ZeroDivisionError("Делить на ноль нельзя")

    x1 = (-b + (b ** 2 - 4 * a * c) / 2 * a) ** 1 / 2
    x2 = (-b - (b ** 2 - 4 * a * c) / 2 * a) ** 1 / 2
    print(f'Корни квадратного уравнения равны: x1={x1} и x2={x2} ')

kva_yr()