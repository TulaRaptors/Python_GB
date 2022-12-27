# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = float(input('Введите число: '))
numb = list(str(number))
numb.remove('.')
sum_digit = sum(map(int, numb))
print(f'Сумма цифр числа {number} = {sum_digit}')
