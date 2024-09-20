import numpy as np
import pandas as pd
import random

# Создадим массив с размером 1000 x 1000 со случными числами от 0 до 100
array = np.random.randint(101, size=(1000,1000))
print(array)


# Найдём среднее значение, минимально и максимальное при помощи NumPy
average = np.average(array)
min = np.min(array)
max = np.max(array)

print(f'Среднее значение:{average} | Минимальное: {min} | Максимальное: {max}')

# Нормилизуем данные по формуле (текущее - мин знач) / (макс знач - мин знач)
normalization = (array - min) / (max - min)
print(normalization)

# Создадим словарь с возрастом и доходом 
data = {'age':[],'profit':[]}

# Сгенерируем данные для вычисления
for i in range(0,1000):
    age = random.randint(18,60)
    profit = random.randint(20000,100000)
    data['age'].append(age)
    data['profit'].append(profit)

# Создадим Датафрейм и выведим
df = pd.DataFrame(data)
print(df)
print(f'Средний возраст:{df[["age"]].mean()}\nСредний доход:{df[["profit"]].mean()}')

# Отсортируем датафрейм и выведим 10 записей
sorted_df = df.sort_values('profit',ascending=False).head(10)
print(sorted_df)


