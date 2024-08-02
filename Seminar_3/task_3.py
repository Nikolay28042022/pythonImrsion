"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""
from itertools import combinations # для комбинаций всех вещей

# Создаем словарь с вещами и их массами
items = {
    "Палатка": 3.5,
    "Спальник": 1.8,
    "Коврик": 0.7,
    "Горелка": 0.5,
    "Посуда": 0.4,
    "Еда": 2.5,
    "Вода": 3.0,
    "Одежда": 2.0,
    "Фонарик": 0.2,
    "Аптечка": 0.6
}

# Функция для поиска всех возможных комбинаций
def find_combinations(items, max_weight):
    valid_combinations = []
    # Проходим по всем возможным количествам вещей, которые можно взять с собой
    for r in range(1, len(items) + 1):
        # Находим все комбинации r вещей
        for combo in combinations(items.items(), r):
            total_weight = sum(item[1] for item in combo)
            # Проверяем, укладывается ли комбинация по весу
            if total_weight <= max_weight:
                valid_combinations.append(combo)
    return valid_combinations

# Максимальная грузоподъемность рюкзака
max_weight = 8.0

# Поиск всех возможных комбинаций
valid_combinations = find_combinations(items, max_weight)

# Выводим все возможные результаты
for combination in valid_combinations:
    print(combination)