# Задача №2
# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число: '))
multipliers = []
i = 2
while n != 1:
    if n % i == 0:
        multipliers.append(i)
        n /= i
        i = 2
    else:
        i += 1

print(f'Простые множители числа: {multipliers}')
