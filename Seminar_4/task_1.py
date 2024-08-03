"""
Напишите функцию для транспонирования матрицы.
"""


def transpose(matrix):
    # Используем функцию zip и распаковку
    return [list(row) for row in zip(*matrix)]


# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose(matrix)
for row in transposed_matrix:
    print(row)
