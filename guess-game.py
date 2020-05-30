# Это игра "угадай число".

import sys
import random


secretNumber = random.randint(1, 20)
print('Привет! Как тебя зовут?')
name = input()
print(f'Итак, {name}, угадай, какое число от 0 до 20 я загадал.')
#print(f'DEBUG: загадано число {secretNumber}')

# Просим игрока угадать число 6 раз.
for guessesTaken in range(1, 7):
    print('Попробуй угадать.')
    guess = ''
    try:
        guess = int(input())
    except ValueError:
        print(f'{name}, нужно было ввести число от 0 до 20')
        continue
    if guess < secretNumber:
        print('Число слишком маленькое')
    elif guess > secretNumber:
        print('Число слишком большое')
    else: break

if guess == secretNumber:
    print(f'Молодец, {name}! Номер угадан c {guessesTaken} попытки!')        
else:
    print(f'Нет, я загадал число {secretNumber}.')
