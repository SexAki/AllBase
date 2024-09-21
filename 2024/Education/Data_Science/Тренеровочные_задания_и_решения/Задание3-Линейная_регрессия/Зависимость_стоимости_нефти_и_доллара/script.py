import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Шаг 1: Загрузка данных
oil_data = pd.read_csv('brent-monthly.csv')  # Задаем правильный разделитель
usd_rub_data = pd.read_csv('usdrub_m.csv')   # Данные с курсом USD/RUB

# Шаг 2: Создание датафрейма
df = pd.DataFrame({
    'oil': oil_data["Price"],   # Цены на нефть
    'us_rub': usd_rub_data['Close']  # Курс USD/RUB
})


# Шаг 3: Очистка данных
df = df.dropna()

# Шаг 4: Разделение данных на обучающую и тестовую выборку
X = df[['oil']]  # Признак (цены на нефть)
y = df['us_rub']  # Целевая переменная (курс USD/RUB)

# Разделяем данные на 80% обучение и 20% тест
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Шаг 5: Обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Шаг 6: Предсказание на тестовых данных
y_pred = model.predict(X_test)

# Шаг 7: Оценка модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2): {r2}")

# Шаг 8: Визуализация
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual data')
plt.plot(X_test, y_pred, color='red', label='Predicted data')
plt.xlabel('Oil Price (Brent)')
plt.ylabel('USD/RUB Exchange Rate')
plt.title('Linear Regression: Brent Oil vs USD/RUB')
plt.legend()
plt.show()
