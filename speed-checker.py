import speedtest
import time
import datetime
import csv
import logging

logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

# TO DO:
# [X] get average from 3
# [ ] automatic startup

logging.debug('Start of program')

try:   
    print("Запускаем Speedtest...")
    speedtester = speedtest.Speedtest()
    print("Начинаем проверку скорости интернета...")
    best_server = speedtester.get_best_server()

    logging.debug('server: %s, %s' % (best_server['name'], best_server['sponsor']))

    tries = []
    for i in range(3):
        tries.append(speedtester.download())
        logging.debug('tries[%s]: %s' % (i, tries[i]))

    avg_speed = sum(tries) / len(tries)

    download_speed = round(avg_speed / 1000000, 2)
    max_speed = round(max(tries) / 1000000, 2)
    min_speed = round(min(tries) / 1000000, 2)



    now = datetime.datetime.now()
    now_date = now.strftime("%d.%m.%Y")
    now_time = now.strftime("%H:%M")

    measurement = [now_date, now_time, download_speed]
    path_to_csv = '/home/mikhail/Desktop/speed-check.csv'

    with open(path_to_csv, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter = ';')
        writer.writerow(measurement)
        
    # print("Дата:", now_date)
    print("Время измерения:", now_time)
    print(f'Скорость загрузки: {download_speed} Мбит/с')
    print(f'Макс/мин: {max_speed}/{min_speed} Мбит/с')
    print(f'Результаты записаны в файл {path_to_csv}')

except speedtest.ConfigRetrievalError as error:
    print('Измерение не выполнено. Нет соединения с интернетом.')

logging.debug('End of program')