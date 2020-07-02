import time
import os

file_path = 'txt/test.txt'

while True:
    if os.path.exists(file_path):
        with open(file_path) as file:
            print(file.read())    
    else:
        print('File does not exists')
    time.sleep(10)

