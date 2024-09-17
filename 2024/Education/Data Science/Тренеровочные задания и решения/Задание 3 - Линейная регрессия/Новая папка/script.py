# Импортируем необходимые библиотеки
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Синтетические данные
data = {
    'Year': np.arange(2000, 2013),
    'Oil_Price': [28, 30, 25, 31, 41, 150, 55, 70, 90, 110, 115, 105, 95],  # цена на нефть в долларах
    'RUB_USD': [28, 29, 30, 31, 28, 27, 126, 25, 24, 22, 20, 24, 26]         # курс рубля к доллару
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Разделим переменные
X = df[['Oil_Price']]  # независимая переменная (цены на нефть)
y = df['RUB_USD']      # зависимая переменная (курс рубля)

# Разделение данных на обучающую и тестовую выборки (80% на обучение, 20% на тест)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создадим объект модели линейной регрессии
model = LinearRegression()

# Обучим модель на обучающей выборке
model.fit(X_train, y_train)

# Сделаем прогнозы на тестовой выборке
y_pred = model.predict(X_test)

# Оценим качество модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R²: {r2:.2f}")

# Вывод коэффициентов модели
print(f"Intercept (Свободный член): {model.intercept_}")
print(f"Coefficient (Коэффициент наклона): {model.coef_[0]}")

# Визуализация результатов
plt.scatter(X_test, y_test, color='black', label='Actual data')
plt.plot(X_test, y_pred, color='blue', linewidth=2, label='Predicted data')
plt.xlabel('Oil Price ($)')
plt.ylabel('RUB/USD Exchange Rate')
plt.title('Oil Price vs RUB/USD Exchange Rate (Test Data)')
plt.legend()
plt.show()
