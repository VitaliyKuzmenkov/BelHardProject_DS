# a = 7
# b = "hello"
# c = 13.4
#
# print(a, b, c)
#
# print(id(a))
#
# print(type(b))
#
# a = "hello"
#
# print(a, b, c)
# print(id(b))
# print(bool(a == b), bool(a == c))

# a = int(input("Введите переменную a- "))
# b = int(input("Введите переменную b- "))
# c = int(input("Введите переменную c- "))
#
# print("a=" + str(a), "b=" + str(b), "c=" + str(c))
#
# print("id(a)=" + str(id(a)),
#       "id(b)=" + str(id(b)),
#       "id(c=)" + str(id(c)))
#
# print("Тип(a)=" + str(type(a)),
#       "Тип(b)=" + str(type(b)),
#       "Тип(c=)" + str(type(c)))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 4, 4, 22]

del lst[5]
lst.remove(3)
lst.append([44, 33, 55])
lst.insert(5, "qwerty")
lst.extend(["ad"])
lst.pop()


lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 4, 4, 22]


print(sorted(lst1, reverse=True))

lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 4, 4, 22]
lst2.clear()
print(lst2)

lst3 = lst1

print(lst3)