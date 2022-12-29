# Задача №3
# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# (если получаются длинные числа после запятой, это нормально и особенность
# данного языка программирования. ваш ответ может не совпадать с примером(может получитя 0,20))
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n = int(input('Введите количество элементов списка: '))
lstr1 = []
lstr2 = []
for i in range(n):
    lstr1.append(round(random.uniform(0, 99), 2))
    lstr2.append(round(lstr1[i] % 1, 2))
print(f'Список из {n} элементов = {lstr1}')

print(f'Разница между min = {min(lstr2)} дробной частью и max = {max(lstr2)} '
      f'дробной частью = {round(max(lstr2) - min(lstr2), 2)}')