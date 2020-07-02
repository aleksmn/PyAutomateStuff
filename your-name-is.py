import random
import time

'''Get your new and awesome name here!'''

def get_name(s):
    return ''.join(random.choices(
        'abcdefgalsdhfasfbsjhvyyasnmvyaszxn' + s*10,
        k = random.randint(5, 9))).title()

print('Hello, stranger!')

old_name = input('What is your name? ')
new_name = get_name(old_name)

print(f'Lets see {old_name}...')
time.sleep(1)
print('Your new name is...')
time.sleep(1)
print(f'{new_name}!')
answer = input('Do you like it? ')
print(f'{answer.capitalize()}??')
time.sleep(1)
print(f'Well, it does not matter {new_name}! Good bye!')


'''
Example:

Hello, stranger!
What is your name? Mike
Lets see Mike...
Your new name is...
Msmvksi!
Do you like it? no
No??
Well, it does not matter Msmvksi! Good bye!
'''
