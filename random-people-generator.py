import random
import csv
from pprint import pprint
from datetime import timedelta, datetime

people = []
m, f = 'муж', 'жен'
genders = [m, f]
last_names = {
    m: ["Иванов", "Петров", "Сидоров","Кузнецов","Попов","Васильев","Соколов","Михайлов","Новиков",],
    f: ["Иванова","Федорова","Морозова","Волкова","Алексеева","Лебедева","Семенова","Егорова","Павлова","Козлова",]}
first_names = {
    m: ["Дмитрий", "Сергей", "Михаил","Артём","Арсений","Даниил","Роман","Кирилл","Никита","Матвей","Андрей",],
    f: ["Людмила","Татьяна","Лариса","Дарья","Виктория","София","Анастасия","Мария","Анна","Полина","Елизавета","Екатерина","Ксения","Валерия","Варвара",]}
father_names = {
    m: ["Петрович","Николаевич","Александрович","Михайлович","Данилович","Романович","Кириллович","Матвеевич","Андреевич",],
    f: ["Петровна","Николаевна","Александровна","Сергеевна","Юрьевна","Матвеевна","Дмитриевна",]}
cities = ["Москва","Нижний Новгород","Саратов","Санкт-Петербург","Тверь","Тула","Самара","Волгоград",]
streets = ["Полевая","Луговая","Садовая","Ленина","Мира","Гагарина","Королева","Профсоюзная",]
departments = ["Бухгалтерия","Учебный","Инженерный","Строительный",]
groups = ["A", "B", "C", "D"]


def get_random_date(start, end):
    '''Возвращает случайную дату между двумя датами в формате '%d.%m.%Y
    Пример. Ввод: random_date('1.1.2001','31.12.2019') Вывод: 24.10.2004'''
    date_format = '%d.%m.%Y'
    d1 = datetime.strptime(start,date_format)
    d2 = datetime.strptime(end,date_format)
    delta_days = (d2 - d1).days
    rand_delta_days = random.randint(0, delta_days)
    new_date = d1 + timedelta(days=rand_delta_days)

    return datetime.strftime(new_date, date_format)


def get_gender(prop_of_males):
    if random.random() > prop_of_males:
        return genders[1]
    return genders[0]
    

def csv_from_list(path_to_csv, list_of_rows):
    '''Функция для создания CSV файла из списка'''
    with open (path_to_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter = ';')
        for _ in list_of_rows:
            writer.writerow(_)
    return print(f'Файл {path_to_csv} создан.')


for _ in range(150):
    address = f'ул. {random.choice(streets)}, д. {random.randint(1,79)}'\
              f'кв. {random.randint(1,129)}'
    gender = get_gender(0.4)
    phone_number = f'+7 ({random.randint(0, 999):03}) {random.randint(0, 999):03}-'\
                   f'{random.randint(0, 99):02}-{random.randint(10, 99)}'
    start_date = get_random_date('1.1.2001','31.12.2019')
    end_date = get_random_date(start_date,'31.05.2020')
    # вторая дата end_date должна быть больше, чем вторая дата в start_date
    department = random.choices(departments, weights=[2,1,1,1])[0]

    people.append([
        random.choice(last_names[gender]),              # фамилия
        random.choice(first_names[gender]),             # имя
        random.choice(father_names[gender]),            # отчество
        gender,                                         # пол
        start_date,                                     # начальная дата
        end_date,                                       # конечная дата
        phone_number,                                   # номер телефона
        random.choice(cities),                          # город
        address,                                        # адрес
        str(random.randint(11111,999999)),              # индекс
        department,                                     # отдел
        'Группа ' + random.choice(groups)])             # группа
              

#pprint(people)
print('Идет запись в файл csv/random_people.csv...')

csv_from_list('csv/random_people.csv', people)
    
print('Запись закончена.')
