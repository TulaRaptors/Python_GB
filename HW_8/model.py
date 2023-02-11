# def export_txt(filename: str, data: list):
#     with open(filename, 'w', encoding='utf-8') as f:
#         for i in range(len(data)):
#             s = f'{data[i]}'
#             f.write(f'{s}\n')


def write_data(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(len(data)):
            s = ''
            for j in data[i].values():
                s += j + ','
            f.write(f'{s[:-1]}\n')


def read_file(filename: str):
    data = []
    fields = ['Фамилия', 'Имя', 'Должность', 'З/П']
    with open(filename, 'r', encoding='utf-8') as f:
        for i in f:
            record = dict(zip(fields, i.strip().split(',')))
            data.append(record)
    return data


def add_employee(data: list, user_data: str):
    fields = ['Фамилия', 'Имя', 'Должность', 'З/П']
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)


def delite_employee(data: list, id: int):
    employee = data[id - 1].get('Фамилия') + ' ' + data[id - 1].get('Имя')
    choiсe = int(input(f'Удалить сотрудника {employee}?\n'
                       '1 - Да\n'
                       '2 - Нет\n'
                       'Вы уверены?: '))
    if choiсe == 1:
        data.pop(id - 1)


def replace_employee(data: list, user_data: str, id: int):
    fields = ['Фамилия', 'Имя', 'Должность', 'З/П']
    record = dict(zip(fields, user_data.split(',')))
    data[id - 1] = record
