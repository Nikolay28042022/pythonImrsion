"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

import os


def parse_file_path(file_path):
    # Получаем путь к каталогу
    directory = os.path.dirname(file_path)
    # Получаем имя файла с расширением
    file_name_with_ext = os.path.basename(file_path)
    # Получаем имя файла
    file_name, file_ext = os.path.splitext(file_name_with_ext)

    return (directory, file_name, file_ext)


# Пример использования
path = "/home/user/documents/example.txt"
result = parse_file_path(path)
print(result)  # Вывод: ('/home/user/documents', 'example', '.txt')


