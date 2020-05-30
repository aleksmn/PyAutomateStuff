def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('You tried to devide by zero')

print(div42by(4))

