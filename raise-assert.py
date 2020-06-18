# Raise an assert statements

import traceback

'''

***********
*         *
*         *
*         *
***********

'''

def boxPrint(symbol, width, height):
    try:
        if len(symbol) != 1:
            raise Exception('"symbol" needs to be a string of length 1.')

        print(symbol * width)

        for i in range(height - 2):
            if i == 1:
                print(symbol + 'Hello!'.center(width - 2) + symbol)
                continue
            print (symbol + (' ' * (width - 2)) + symbol)

        print(symbol * width)
    except:
        errorFile = open('error_log.txt', 'a')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written in error_log.txt')

boxPrint('*', 15, 5)


