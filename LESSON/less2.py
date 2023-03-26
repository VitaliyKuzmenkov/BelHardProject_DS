# import random
# lst = [random.randint(0,100) for i in range(20)]
# s = sum(lst)
# n = len(lst)
# sr = s/n
#
# print(lst)
# print(len(lst))
# print(sr)
#
# lst1 = [random.randint(-8,10) for i in range(10)]
#
# print(lst1)
#
# lst2 = [random.randint(-8,10) for i in range(15)]
#
# print(lst2)
#
# set1 = set(lst1)
# set2 = set(lst2)
# set3 = list(set1.symmetric_difference(set2))
# print(set3)
# print(sorted(list(set3),reverse=True))

# m = min(lst2)
# ind = lst2.index(m)
# del lst2[:ind]
# print(lst2)

# lst3 = [random.randint(-10,10) for i in range(10)]
# print(lst3)
# print(sorted(lst3, reverse=True))

# a = "aassshhhddd"
#
# s = set(a)
#
# print(s, len(s))

# seq = "1234567"
# f_set = frozenset(seq)
# print(hash(f_set))  # адрес памяти
# print(f_set)
#
# d = {1: "a", 2: "f"}
# f = dict([
#     ("g","r")
# ])
# d["j"] = "n"
#
# print(len(d))
# print(d)
# print(f.get("g"))
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))
# d.update(f)
# print(d)
#
# d_1 = {1:"a", 2:"b", 3: "4c"}
# d_2 = {3: "d", 5: "e", 6: "f"}
#
#
# d_1_keys = set(d_1.keys())
# d_2_keys = set(d_2.keys())
#
# print(d_2_keys.intersection(d_1_keys))
# print(d_2_keys.symmetric_difference(d_1_keys))
