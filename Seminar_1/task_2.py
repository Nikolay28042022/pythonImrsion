"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""
def is_prime(number):
    """Функция для проверки, является ли число простым."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    """Основная функция для запроса числа и вывода результата."""
    try:
        number = int(input("Введите число (от 0 до 100000): "))
        if number < 0 or number > 100000:
            print("Число должно быть в диапазоне от 0 до 100000.")
            return

        if is_prime(number):
            print(f"Число {number} является простым.")
        else:
            print(f"Число {number} является составным.")
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")


if __name__ == "__main__":
    main()
