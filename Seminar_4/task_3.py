"""
Напишите программу банкомат.
Начальная сумма равна нулю.
Допустимые действия: пополнить, снять, выйти.
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третьей операции пополнения илли снятия начисляются проценты - 3%
Нельзя снять больше, чем на счете.
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ощибочной.
Любое действие выволит сумму денег.
Все операции поступления и снятия средств сохраняйте в отдельный список.
Разбейте задачу на отдельные функции.
"""

balance = 0
operations = []
operation_count = 0


def deposit(amount):
    global balance, operation_count
    if amount % 50 != 0:
        print("Сумма пополнения должна быть кратна 50.")
        return
    balance += amount
    operations.append(f"Пополнение: +{amount} у.е.")
    operation_count += 1
    apply_wealth_tax()
    check_bonus()
    print_balance()


def withdraw(amount):
    global balance, operation_count
    if amount % 50 != 0:
        print("Сумма снятия должна быть кратна 50.")
        return
    if amount > balance:
        print("Недостаточно средств на счете.")
        return

    fee = max(30, min(amount * 0.015, 600))
    total_withdrawal = amount + fee

    if total_withdrawal > balance:
        print("Недостаточно средств для снятия с учетом комиссии.")
        return

    balance -= total_withdrawal
    operations.append(f"Снятие: -{amount} у.е. (Комиссия: {fee:.2f} у.е.)")
    operation_count += 1
    apply_wealth_tax()
    check_bonus()
    print_balance()


def apply_wealth_tax():
    global balance
    if balance > 5_000_000:
        tax = balance * 0.10
        balance -= tax
        operations.append(f"Налог на богатство: -{tax:.2f} у.е.")


def check_bonus():
    global balance, operation_count
    if operation_count % 3 == 0:
        bonus = balance * 0.03
        balance += bonus
        operations.append(f"Бонус за 3 операции: +{bonus:.2f} у.е.")


def print_balance():
    global balance
    print(f"Текущий баланс: {balance:.2f} у.е.")


def exit_program():
    global balance, operations
    print("Завершение работы.")
    print_balance()
    print("История операций:")
    for operation in operations:
        print(operation)
    exit()


# Пример использования:
deposit(150)  # Пополнение
withdraw(50)  # Снятие
deposit(100)  # Пополнение
exit_program()  # Завершение работы
