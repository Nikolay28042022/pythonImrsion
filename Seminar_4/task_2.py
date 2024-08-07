"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
"""


def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            # Пытаемся использовать значение в качестве ключа
            result[value] = key
        except TypeError:
            # Если значение не хешируемое, используем его строковое представление
            result[str(value)] = key
    return result

# Пример использования:
print(create_dict(a=42, b=[1, 2, 3], c="hello", d={'key': 'value'}))
