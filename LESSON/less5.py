import pandas as pd, matplotlib
# import csv

# import random
#
# data = [random.randint(0, 100) for elem in range(5)]
#
# file = open('test_data.txt', 'r+')
#
# print(file.name, file.mode, file.encoding)
#
# print(file.read(100))  # колиичество символов
# print(file.readline())

# file.close()
# print(file.closed)

# while file: # перебираем строки файла
#     row = file.readline()
#     if row:
#         print(row)
#     break
# file.write("fbfkhfk")
#
# print(file.read())
#
# file.close()

# with open('data.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#
# writer = csv.writer(f)
# writer.writerows("14, 15, 16")


"""Задача"""


# with open('test_data.txt', 'r+') as f:
#     # print(f.read())
#     data = f.readlines()
#     for num in data:
#         print(num.replace("\n",''))
#     print(len(data))


# f = open('test_data.txt', 'r+')
# f.seek(2)
# f.write("dvv")
# f.close()

"""pandas"""


# california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
# print(california_housing_dataframe.describe())
# california_housing_dataframe.hist('housing_median_age')
#
# # df = pd.read_html("https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%81%D1%82%D0%BE%D0%BB%D0%B8%D1%86_%D0%A1%D0%A8%D0%90#%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D1%81%D1%82%D0%BE%D0%BB%D0%B8%D1%86%D1%8B_%D0%A1%D0%A8%D0%90")
# df1 =pd.read_json("https://data.smcgov.org/resource/mb6a-xn89.json")
# print(df1.head())

df = pd.read_csv('data.csv')
print(df.describe())
