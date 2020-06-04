# Find total size of files in current directory

import os
import send2trash

#os.path.abspath('../') # '/home/mikhail/Code'

#os.path.getsize('/home/mikhail/Code/PandasDemo/Snippets.ipynb') # 16604
#os.listdir()

totalSize = 0

def getPathToFile(filename):
    return os.path.join(os.getcwd(), filename)

for filename in os.listdir():
	if not os.path.isfile(getPathToFile(filename)):
		continue
	totalSize += os.path.getsize(getPathToFile(filename))
	
print(f'Текущая рабочая директория: {os.getcwd()}')
print(f"Общий размер файлов в директории: {totalSize} Байт")

