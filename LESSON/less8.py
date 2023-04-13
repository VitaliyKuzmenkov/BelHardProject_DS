import random


def cat_voice():
    return ('Meow!')


def dog_voice():
    return ('Woof!')


print(dog_voice())
print(cat_voice())


def get_voice(text):
    return (f'Hello, {text} !')


print(get_voice('Vitaliy'))


def gen(a,b,c):
    num = []
    for i in range(c):
        num_elem = random.randint(a, b)
        if num_elem % 2 == 0:
            num.append(num_elem)
    return num


print(gen(1,9,10))


def gen_1(a,b):
    num = []
    num = [i for i in range(a, b) if i % 2 == 0]
    return num


print(gen_1(1,9))


name_gef = lambda name: f"Hello {name} !"

print(name_gef("efjf"))

data = ["ndvkldnsvkdj", "kdbwbhdkh"]
res = list(map(len, data))
print(res)

data_1 = [1, 2, 3]
res_1 = int(map(list, data_1))
print(res_1)