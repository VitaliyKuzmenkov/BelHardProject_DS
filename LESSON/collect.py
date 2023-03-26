from collections import namedtuple, deque, ChainMap, Counter

NTuple = namedtuple('NTuple', ['attr_1', 'attr_2'])

n = NTuple(attr_1="A", attr_2="B")

print(n.attr_1, n.attr_2)
print(n[0], n[1])


lst = deque([1, 2, 3], maxlen=4)
lst.insert(0, 9)
lst.extend([8, 9, 5, 7])
print(lst)

d_1 = {1:"a", 2:"b", 3: "4c"}
d_2 = {3: "d", 5: "e", 6: "f"}
d_3 = {8: "hgh"}
c_map = ChainMap(d_1, d_2, d_3)
print(c_map)
print(c_map[3])

str = input("Ведите текст:  ")

cent = int(len(str)/2)
print(str[cent])
if str[0] == str[cent]:
    print(str[1:-1])
