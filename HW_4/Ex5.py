# Задача №5
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random


def rnd():
    return random.randint(0, 10)


def create_dict(st):  # Создаем словарь с ключами и рандомными коэффициентами
    rand_dic = []
    for i in range(st + 1):
        couple = []
        kf = rnd()
        if kf != 0:
            couple.append(i)
            couple.append(kf)
            rand_dic.append(couple)
    return dict(rand_dic)


def create_polinom(d):  # Создаем многочлен в виде строки
    lst = ''
    for k in range(max(d.keys()), -1, -1):
        z = False
        kf = d.get(k)

        if k > 1 and k in d:
            lst += f'{kf}*x^{k}'
            z = True
        elif k == 1 and k in d:
            lst += f'{kf}*x'
            z = True
        elif k == 0 and k in d:
            lst += f'{kf}'
        elif k == 0 and k not in d:
            lst = lst[:-3]

        if z:
            lst += ' + '

    if len(lst) > 2:
        lst += ' = 0'
    return lst


def parsing_mn(st_old):  # Разбираем многочлен на словарь по степеням
    st = st_old[:(len(st_old) - 3)].replace(' ', '').replace('*', '').split('+')
    dic_mn = []
    for i in range(len(st)):
        couple = []
        if 'x^' in st[i]:
            j = st[i].find('^')
            couple.append(int(st[i][j + 1:]))
            couple.append(int(st[i][:j - 1]))
        elif ('x' in st[i]) and ('^' not in st[i]):
            j = st[i].find('x')
            couple.append(1)
            couple.append(int(st[i][:j]))
        else:
            couple.append(0)
            couple.append(int(st[i]))
        dic_mn.append(couple)
    return dict(dic_mn)


mn1 = create_polinom(create_dict(int(input('Введите для 1-ого многочлена степень k = '))))
mn2 = create_polinom(create_dict(int(input('Введите для 2-ого многочлена степень k = '))))

with open('file5_1.txt', 'w') as data:
    data.write(mn1)
with open('file5_2.txt', 'w') as data:
    data.write(mn2)

with open('file5_1.txt', 'r') as data:
    st1 = data.read()
with open('file5_2.txt', 'r') as data:
    st2 = data.read()

pp1 = parsing_mn(st1)
pp2 = parsing_mn(st2)
pp3 = pp1.copy()
pp3.update(pp2)
for key in pp3:
    if key in pp1 and key in pp2:
        pp3[key] = pp1.get(key) + pp2.get(key)
st_res = create_polinom(pp3)

with open('file5_result.txt', 'w') as data:
    data.write(st_res)

print(f'Первый многочлен: {st1}')
print(f'Второй многочлен: {st2}')
print(f'Сумма многочленов: {st_res}')
