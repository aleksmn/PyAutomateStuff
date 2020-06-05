import speedtest
import time
import datetime

speedtester = speedtest.Speedtest()
best_server = speedtester.get_best_server()
download_speed = round(speedtester.download() / 1000000, 2)

now = datetime.datetime.now()
now_date = now.strftime("%d.%m.%Y")
now_time = now.strftime("%H:%M")

print("Дата:", now_date)
print("Время:", now_time)
print(f'Скорость загрузки: {download_speed} Мбит/с')
