"""
 Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать
 “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
import random

def guess_the_number():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000

    num = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    attempts = 10

    print("Программа загадала число от 0 до 1000. Угадайте его за 10 попыток!")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Попытка {attempt}: Введите ваше предположение: "))

        if guess < num:
            print("Больше")
        elif guess > num:
            print("Меньше")
        else:
            print(f"Поздравляем! Вы угадали число {num} с {attempt} попытки!")
            break
    else:
        print(f"К сожалению, вы не угадали число. Загаданное число было {num}.")

if __name__ == "__main__":
    guess_the_number()
