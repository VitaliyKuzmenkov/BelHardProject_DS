import pandas as pd
import csv
import json

"""На основе файла example.csv создать JSON  с помощью Pandas.
Получить среднее значение для каждой колонки файла.
"""

with open('automobile.csv', 'w') as csvfile:
    columns = ['Date', 'Model', 'Mark', 'Power']
    data = [
        ['2023-04-04', 'BMW', 'IX', 250],
        ['2023-04-05', 'AUDI', 'e - tron', 200],
        ['2023-04-06', 'Tesla', 'Model X', 350],
        ['2023-04-07', 'Mersedes', 'EQC', 450]
    ]

    df = pd.DataFrame(data, columns=columns)
    df.to_csv(r'automobile.csv')
    print('DataFrame\n----------')
    print(df)
    mean = df['Power'].mean()
    print('\nMean\n------')
    print(mean)

mydata = {}

with open('automobile.csv', encoding='utf-8') as csv_file:
    csvRead = csv.DictReader(csv_file)

    for rows in csvRead:
        mykey = rows['Date']
        mydata[mykey] = rows

        with open('mydatalist.json', 'w+', encoding='utf-8') as jsonfile:
            jsonfile.write(json.dumps(mydata, indent=4))

print(mydata)
