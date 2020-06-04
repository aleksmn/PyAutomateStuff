import random
from pprint import pprint

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

for _ in range(4):
    address = f'ул. {random.choice(streets)}, д. {random.randint(1,79)} кв. {random.randint(1,129)}'
    gender = random.choice(genders)
    

    people.append([
        random.choice(last_names[gender]),
        random.choice(first_names[gender]),
        random.choice(father_names[gender]),
        gender,
        random.choice(cities),
        address,
        random.choice(departments),])


pprint(people)
