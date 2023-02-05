# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

number = int(input('Введите число: '))
posl_list = list(map(lambda x: round((1 + 1 / x) ** x, 2), [i for i in range(1, number + 1)]))
print(f'Последовательность для {number} чисел: {posl_list}')
print(f'Сумма чисел последовательности = {round(sum(posl_list), 2)}')
