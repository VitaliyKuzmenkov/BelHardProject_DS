import pandas as pd
import csv
import json
import xml
import openpyxl

"""Получить подробную информацию о датафрейме (count, mean, std, min, 
25%, 50%, 75%, max). . Полученный датафрейм транспонировать Также
вывести список колонок датафрейма и информацию о типах данных 
колонок датафрейма На основе полученной информации создать . 
датафрейм и записать его в формате JSON."""


df = pd.read_csv('6_class_csv.csv')
df_info = df.info()
df_new = pd.DataFrame(df_info)
print(df.describe())
print(df.describe().transpose())
print(df.info())

with open('6_class_csv_new.csv', 'w+') as csvfile:
    df_new.to_csv(r'6_class_csv_new.csv')


"""Вычислить среднее значение колонки и добавить новую Temperature 
колонку в которой хранится модуль разности текущей delta_T, 
Temperature . NaN и средней Проверить содержит ли датафрейм
значения Вычислить максимальное значение Вернуть . Temperature. 
датафрейм в котором и delta_T <= Tmax/2 Temperature >= delta_Tmin. 
Полученный датафрейм сохранить в формате CSV"""

mean_temp = df['Temperature (K)'].mean()
print(mean_temp)
df["delta_T"] = (df['Temperature (K)'] - df['Temperature (K)'].mean())
print(df.info())
max_temp = df['Temperature (K)'].max()
mean_temp_min = df['delta_T'].min()
print(max_temp)
df_new = df[(df['delta_T'] <= max_temp/2) & (df['Temperature (K)'] >= mean_temp_min)]
print(df_new)
print(df)

with open('6_class_csv_new.csv', 'w+') as csvfile:
    df_new.to_csv(r'6_class_csv_new.csv')

"""Вычислить коэффициент корреляции датафрейма Вычислить . 
среднее значение для каждого Absolute magnitude(Mv) Star type. 
Вычислить количество записей для каждого спектрального класса """



test1_df = df.groupby('Star type')['Absolute magnitude(Mv)'].mean()
print('')
print('среднее значение для каждого Absolute magnitude(Mv) Star type.')
print(test1_df)


number_spectral_class = df["Spectral Class"].value_counts()
print('')
print('количество записей для каждого спектрального класса')
print(number_spectral_class)

"""Для каждого спектрального класса вычислить дисперсию для 
Luminosity(L/Lo), Absolute стандартная ошибка среднего для Absolute
magnitude(Mv)  и среднеквадратичное отклонение для Temperature. На
основе данных создать датафрейм и записать в файл excel """


test2_df = df.groupby('Spectral Class')['Luminosity(L/Lo)'].var()
print('')
print('дисперсию для Luminosity(L/Lo)')
print(test2_df)

test2_df.to_excel(r'6_class_csv_new.xlsx')

test3_df = df.groupby('Spectral Class')['Absolute magnitude(Mv)'].sem()
print('')
print('стандартная ошибка среднего для Absolute magnitude(Mv)')
print(test3_df)

test3_df.to_excel(r'6_class_csv_new.xlsx')


test4_df = df.groupby('Spectral Class')['Temperature (K)'].std()
print('')
print('среднеквадратичное отклонение для Temperature')
print(test4_df)

df_merged_2_3_4 = pd.concat([test2_df, test3_df, test4_df], axis=1)

with open('6_class_csv_new.xlsx', 'r+') as xls_file:
    df_merged_2_3_4.to_excel(r'6_class_csv_new.xlsx')

"""На основании датасета создать новый датафрейм с двумя df new_df 
колонками и где Temperature temperature_C, 
new_df["Temperature"] = df["Temperature"]
а в колонке хранится значение температуры в С temperature_C .
Соединить два датафрейма в один как минимум тремя разными , 
способами.
После соединения проверить датафрейм на наличие значений NaN . 
Заменить отсутствующие данные следующими способами :
1. Для всех значений установить среднее значение столбца NaN . 
2. Заменить значения с помощью интерполяции NaN .
3. Удалить строки содержащие значения"""

df_new_tempr = df.copy()
df_new_tempr.drop(df.columns[[1, 2, 3, 4, 5, 6, 7]], axis=1, inplace=True)
print(df_new_tempr.info())
df_new_tempr["Temperature_C"] = (df['Temperature (K)'] + 273)
print(df_new_tempr.info())
result_df_1 = pd.merge(df, df_new_tempr, how="inner",  on='Temperature (K)')
print(result_df_1.info())
result_df_2 = pd.concat([df, df_new_tempr], axis=1, join='outer')
print(result_df_2.info())
result_df_3 = pd.merge(df, df_new_tempr, how="outer")
print(result_df_1.info())
