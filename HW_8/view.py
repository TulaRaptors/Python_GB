def show_menu():
    print('\nГлавное меню:\n'
          '1 - Найти сотрудника\n'
          '2 - Сделать выборку сотрудников по должности\n'
          '3 - Сделать выборку сотрудников по зарплате\n'
          '4 - Добавить сотрудника\n'
          '5 - Удалить сотрудника\n'
          '6 - Обновить данные сотрудника\n'
          '7 - Экспорт данных в json\n'
          '8 - Экспорт данных в csv\n'
          '9 - Закончить работу')
    return int(input('Выберите пункт меню: '))


def print_data(data: list):
    if len(data) != 0:
        print('\nСписок сотрудников: ')
        for i in data:
            print(f'id = {data.index(i) + 1}')
            s = ''
            for a, b in i.items():
                s += f'{a}: {b}\n'
            print(s)
    else:
        print('\nНе найдено')


def new_employee():
    print('\nДанные сотрудника')
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    post = input('Введите должность: ')
    wages = input('Введите з/п: ')
    return f'{last_name},{first_name},{post},{wages}'
