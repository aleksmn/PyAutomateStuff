import csv

def csv_from_list(path_to_csv, list_of_rows):
    '''Функция для создания CSV файла из списка'''
    with open (path_to_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter = ';')
        for _ in list_of_rows:
            writer.writerow(_)
    return print(f'Файл {path_to_csv} создан.')


with open('csv/lastnames_orig.txt', newline='') as file:
    all_text = file.read()

cells = all_text.split(' ')

lines = list(zip(*(iter(cells),) * 3)) # Разделяем список на группы по 3.

csv_from_list('csv/lastnames.csv', lines)


