
def count_char(char, filepath='txt/bear.txt'):
    with open(filepath) as file:
        return file.read().count(char)

def append_to_file(string, filepath='txt/test.txt'):
    with open(filepath, 'a+') as f:
        f.write('\n' + string)
        f.seek(0)
        file_end = f.read()[-80:]

    print(f'Файл {filepath} обновлен.\n'
          f'Теперь файл заканчивается на:\n{file_end}')
        

string = 'My string to append'

append_to_file(string, 'txt/test2.txt')