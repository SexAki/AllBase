import random
import matplotlib.pyplot as plt

def function():
    max_var = 1  # Максимальный шаг
    pos = 0      # Начальная позиция
    var = 0.5    # Шаг
    rand = loop()  # Генерация случайного числа
    pos_history = [pos]  # История позиций для построения графика

    print(f"Целевая точка: {rand}")

    while abs(pos - rand) > 0.5:  # Условие завершения, если pos близко к rand
        if rand < pos:
            pos = pos - var
            if pos < rand:
                pos = rand
        else:
            pos = pos + var
            if pos > rand:
                pos = rand
        
        pos_history.append(pos)  # Сохраняем текущее значение позиции

        # Управление изменением шага
        if var <= max_var:
            var = var * 1.1  # Увеличиваем шаг, если он меньше максимального
        else:
            var = var * 0.9  # Уменьшаем шаг, если он превышает максимальный

    print(f"Достигнута позиция: {pos}")

    # Визуализация
    plt.figure(figsize=(10, 6))
    plt.plot(pos_history, marker='o', label='Траектория движения')
    plt.axhline(y=rand, color='r', linestyle='--', label='Целевая точка')
    plt.title('Движение к целевой точке')
    plt.xlabel('Шаги')
    plt.ylabel('Позиция')
    plt.legend()
    plt.grid(True)
    plt.show()

def loop():
    return random.randint(-25,25)

function()
