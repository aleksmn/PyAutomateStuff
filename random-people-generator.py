import random
from pprint import pprint
from datetime import timedelta, datetime

people = []
m, f = 'муж', 'жен'
genders = [m, f]
last_names = {
    m: ["Иванов", "Петров", "Сидоров"],
    f: ["Иванова", "Петрова", "Сидорова"]}
first_names = {
    m: ["Дмитрий", "Сергей", "Михаил"],
    f: ["Людмила","Татьяна","Лариса","Дарья","Виктория",]}
father_names = {
    m: ["Петрович","Николаевич","Александрович"],
    f: ["Петровна","Николаевна","Александровна","Сергеевна","Юрьевна",]}
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
    

for _ in range(10):
    address = f'ул. {random.choice(streets)}, д. {random.randint(1,79)}'\
              f'кв. {random.randint(1,129)}'
    gender = get_gender(0.2)
    phone_number = f'+7 ({random.randint(0, 999):03}) {random.randint(0, 999):03}-'\
                   f'{random.randint(0, 99):02}-{random.randint(10, 99)}'
    start_date = get_random_date('1.1.2001','31.12.2019')
    end_date = get_random_date(start_date,'31.05.2020')
    # вторая дата end_date должна быть больше, чем вторая дата в start_date

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
        random.choices(departments, weights=[2,1,1,1]), # отдел
        'Группа ' + random.choice(groups)])             # группа
              


pprint(people)

##for _ in people:
##    print (_[3])


