import pandas as pd

# Чтение данных
data1 = pd.read_csv('stats/tf2_stats 1.csv')
data2 = pd.read_csv('stats/tf2_stats 2.csv')

# Список для хранения различий
differences = []

# Поиск различий
for i in range(len(data1)):
    if data1['Value'][i] != data2['Value'][i]:
        name = data1["Statistic Name"][i]
        value1 = data1['Value'][i]
        value2 = data2['Value'][i]
        result = value2 - value1
        
        # Условие для фильтрации по оперделённому классу "Spy" или "SPY"
        if 'Spy' in name or 'SPY' in name:
            differences.append({'name': name, 'value': int(result)})

# Создание DataFrame
df = pd.DataFrame(differences)

# Вывод
df.to_csv(fr'ready\Stats 2.csv')
