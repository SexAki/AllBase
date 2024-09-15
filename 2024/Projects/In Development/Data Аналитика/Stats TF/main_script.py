import requests
import csv
import datetime
import time
def date_time_func():
    # Ваш ключ Steam API и Steam ID пользователя
    API_KEY = ''
    STEAM_ID = ''

    # URL для получения статистики TF2
    url = f"http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=440&key={API_KEY}&steamid={STEAM_ID}"

    # Выполняем запрос к Steam API-**
    response = requests.get(url)
    data = response.json()

    # Проверяем, что запрос успешен
    if 'playerstats' in data:
        stats = data['playerstats']['stats']
        current_time = datetime.datetime.now()
        year = current_time.year
        month =current_time.month
        day = current_time.day
        hour = current_time.hour
        date_time = str(f'{year}-{month}-{day} {hour}')
        # Открываем CSV файл для записи данных
        with open(fr'stats\tf2_stats {date_time}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Записываем заголовок (имя статистики и значение)
            writer.writerow(['Statistic Name', 'Value'])
            
            # Записываем каждую статистику в CSV файл
            for stat in stats:
                writer.writerow([stat['name'], stat['value']])
        
        print("Данные успешно записаны в tf2_stats.csv")
    else:
        print("Не удалось получить данные. Проверьте правильность Steam ID и API ключа.")







def loop():
    while True:
        date_time_func()
        time.sleep(3600)

loop()