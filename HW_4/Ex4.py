# Задача №4
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

st = int(input('Введите степень k = '))
lst = ''
for k in range(st, -1, -1):
    z = False
    koef = random.randint(0, 100)

    if k > 1 and koef != 0:
        lst += f'{koef}*x^{k}'
        z = True
    elif k == 1 and koef != 0:
        lst += f'{koef}*x'
        z = True
    elif k == 0 and koef != 0:
        lst += f'{koef}'
    elif k == 0 and koef == 0:
        lst = lst[:-3]

    if z == True:
        lst += ' + '

if len(lst) > 2:
    lst += ' = 0'

with open('file4.txt', 'w') as data:
    data.write(lst)

# print(lst)
