# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint


def take_candy(player):
    x = int(input(f'{player}, сколько берете конфет? : '))
    while x < 1 or x > 28:
        print('Так нельзя!')
        x = int(input(f'{player}, введите количество от 1 до 28: '))
    return x


player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
value = 2021
print(f'На столе лежит {value} конфета')
print('Игроки по очереди берут не более 28 конфет. Побеждает тот, чей ход последний!')
queue = randint(0, 1)
print('Первый ходит - ', end='')
if queue:
    print(player1)
else:
    print(player2)

while value > 28:
    if queue:
        k = take_candy(player1)
        value -= k
        queue = False
        print(f'Осталось конфет: {value}')
    else:
        k = take_candy(player2)
        value -= k
        queue = True
        print(f'Осталось конфет: {value}')

if queue:
    winner = player1
else:
    winner = player2
print(f'Выиграл {winner}! Поздравляем все конфеты твои!')
