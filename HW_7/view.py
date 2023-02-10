def show_menu():
    print('\nГлавное меню:\n'
          '1 - Показать справочник\n'
          '2 - Создать новый контакт\n'
          '3 - Найти номер\n'
          '4 - Экспорт в txt\n'
          '0 - Выход')
    return input('Выберите пункт меню: ')


def print_phonebook(data: list):
    print('\nСписок контактов: ')
    for i in range(len(data)):
        print(f'{i+1}. {data[i]}')


def user_contact():
    print('\nСоздать новый контакт')
    name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return f'{name} | {phone_number}'
