import speedtest
import time
import datetime
import csv

try:   
    print("Запускаем Speedtest...")
    speedtester = speedtest.Speedtest()
    print("Начинаем проверку скорости интернета...")
    best_server = speedtester.get_best_server()
    download_speed = round(speedtester.download() / 1000000, 2)

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
    print("Результаты записаны в файл", path_to_csv)
    print('')

except speedtest.ConfigRetrievalError as error:
    print('Измерение не выполнено. Нет соединения с интернетом.')
