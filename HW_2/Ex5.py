# Реализуйте алгоритм перемешивания списка.
# (рандомно поменять местами элементы списка между собой)

import random


def mixed(mix_list):
    length = len(mix_list)
    for i in range(length):
        index = random.randint(0, length-1)
        a = mix_list[i]
        mix_list[i] = mix_list[index]
        mix_list[index] = a
    return mix_list


n = int(input('Введите количество элементов: '))
lstr = []
for i in range(n):
    lstr.append(random.randint(-99, 99))
print(f'               Список из {n} элементов: {lstr}')
print(f'   Методом Mixed перемешанный список: {mixed(lstr)}')

random.shuffle(lstr)
print(f'Функцией Shuffle перемешанный список: {lstr}')
