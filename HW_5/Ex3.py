# Создайте программу для игры в ""Крестики-нолики"".
import random


def print_maps():
    print(f' {maps[0]} | {maps[1]} | {maps[2]}')
    print('-----------')
    print(f' {maps[3]} | {maps[4]} | {maps[5]}')
    print('-----------')
    print(f' {maps[6]} | {maps[7]} | {maps[8]}')


def step_maps(step, symbol):
    i = step - 1
    maps[i] = symbol


def get_result():
    win = ''
    victories = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [0, 4, 8],
                 [2, 4, 6]]
    for i in victories:
        if maps[i[0]] == 'X' and maps[i[1]] == 'X' and maps[i[2]] == 'X':
            win = 'X'
        if maps[i[0]] == 'O' and maps[i[1]] == 'O' and maps[i[2]] == 'O':
            win = 'O'
    return win

game_over = False
if input('Первый ход ваш? Да/Нет: ') == 'Да':
    human = True
    player = 'X'
    bot = 'O'
else:
    print('Первым ходит компьютер')
    human = False
    player = 'O'
    bot = 'X'
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
print('Схема игрового поля: ')
print_maps()
for i in range(9):
    maps[i] = ' '

while game_over == False:
    if human == True:
        symbol = player
        step = int(input('Ваш ход: '))
        while maps[step - 1] != ' ':
            print('Поле занято!')
            step = int(input('Ваш ход: '))
    else:
        symbol = bot
        print(f'Компьютер "{symbol}" делает ход: ')
        step = random.randint(1, 9)
        while maps[step - 1] != ' ':
            step = random.randint(1, 9)

    if step != ' ':
        step_maps(step, symbol)
        win = get_result()
        if win != '':
            game_over = True
    else:
        print("Ничья!")
        game_over = True
    print_maps()
    human = not human
print(f'Победил {win}')
