"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""
from fractions import Fraction

def parse_fraction(fraction_str):
    return Fraction(fraction_str)

def sum_and_product_of_fractions(fraction1, fraction2):
    f1 = parse_fraction(fraction1)
    f2 = parse_fraction(fraction2)

    sum_result = f1 + f2
    product_result = f1 * f2

    return sum_result, product_result

if __name__ == "__main__":
    fraction1 = input("Введите первую дробь (например, 'a/b'): ")
    fraction2 = input("Введите вторую дробь (например, 'a/b'): ")

    sum_result, product_result = sum_and_product_of_fractions(fraction1, fraction2)

    print(f"Сумма дробей: {sum_result}")
    print(f"Произведение дробей: {product_result}")
