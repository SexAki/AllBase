import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt


data = {
    'age': np.random.randint(18,60,1000),
    'profit': np.random.randint(20000,100000,1000)
    }

# Сгенерируем данные для вычисления


# Создадим Датафрейм и выведим
df = pd.DataFrame(data)
print(df)

#Гистограмма распределения возрастов
plt.hist('age',data=df, bins=40, color='skyblue', edgecolor='black')
plt.show()

#Диаграмму рассеяния
plt.scatter(data=df,x='age',y='profit')
plt.show()

# Определим количество людей
num_people = len(df)

# Рассчитаем, сколько людей в каждой группе
num_bachelor = int(0.6 * num_people)
num_master = int(0.3 * num_people)
num_phd = num_people - (num_bachelor + num_master)  # Остаток на PhD

sum_people = [num_bachelor,num_master,num_phd]
name_people = ['Bachelor','Master','PhD']

# Создадим список уровней образования
education_levels = ['Bachelor'] * num_bachelor + ['Master'] * num_master + ['PhD'] * num_phd

# Перемешаем значения случайным образом
random.shuffle(education_levels)

# Добавим этот список как новую колонку в DataFrame
df['education_level'] = education_levels

# Проверим первые несколько строк
print(df.head())

# Круговая диаграмма
plt.pie(sum_people, labels=name_people, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.axis('equal')  # Чтобы круг был "круглым", а не овальным
plt.show()

#Корреляция между возрастом и доходом
print(np.corrcoef(df['age'], df['profit']))

