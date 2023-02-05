# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в отдельном списке
# (пример n=4, lst1=[4,-2,1,3]- список на основе n, а позиции элементов lst2=[3,1].

import random

n = int(input('Введите количество элементов: '))
lstr1 = [random.randint(-n, n) for i in range(n)]
print(f'Список из {n} элементов из интервала [-{n},{n}] = {lstr1}')

k = int(input('Сколько позиций хотите перемножить? : '))
lstr2 = [int(input('Введите позицию: ')) for i in range(k)]

lstr3 = [lstr1[lstr2[i]] for i in range(k)]
lstr4 = list(zip(lstr2, lstr3))

pr = 1
for i in lstr2:
    pr *= lstr1[i - 1]
print(f'Произведение элементов {lstr4} = {pr}')
