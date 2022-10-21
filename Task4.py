"""
Напишите функцию read_last(lines, file),
которая будет открывать определенный файл file
и выводить на печать построчно последние строки
в количестве lines (на всякий случай проверим,
что задано положительное целое число).
"""


def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
        else:
            print('Введите положительное целое число строк')


read_last(5, 'file.txt')
read_last(-5, 'file.txt')
