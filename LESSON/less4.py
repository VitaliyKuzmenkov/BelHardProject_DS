# age = 25
#
# print(age > 5)


# lst = [1,22,3,4,5]
# if lst:
#     print(lst)
# else:
#     print("list empty")

# n = int(input())
#
# data = [1, 2, 3, 4, 5, 6]
#
# res = [elem * n for elem in data] if n % 2 == 0 else data * int(n)
#
# print(res)

season = int(input("Введите пару года  "))

seasons = {
    1: 'Зима',
    2: 'Весна',
    3: 'Лето',
    4: 'Осень'
}

print(seasons.get(season))