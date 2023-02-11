from view import show_menu, print_data, new_employee
from model import write_data, read_file, add_employee, delite_employee, replace_employee
from search import find_employee, find_choice, find_by_id
from export import export_json, export_csv


def start():
    choice = show_menu()
    data = read_file('data.csv')

    while choice != 9:
        if choice == 1:
            field = find_choice()
            name = input('\nВведите данные для поиска: ')
            find_list = find_employee(data, name, field)
            print_data(find_list)
        elif choice == 2:
            post = input('\nВведите должность для поиска: ')
            find_list = find_employee(data, post, 'Должность')
            print_data(find_list)
        elif choice == 3:
            post = input('\nВведите З/П для поиска: ')
            find_list = find_employee(data, post, 'З/П')
            print_data(find_list)
        elif choice == 4:
            add_employee(data, new_employee())
            write_data('data.csv', data)
        elif choice == 5:
            pers_id = int(input('Введите id сотрудника: '))
            employee = find_by_id(data, pers_id)
            print_data(employee)
            delite_employee(data, pers_id)
            write_data('data.csv', data)
        elif choice == 6:
            pers_id = int(input('Введите id сотрудника: '))
            employee = find_by_id(data, pers_id)
            print_data(employee)
            replace_employee(data, new_employee(), pers_id)
            write_data('data.csv', data)
        elif choice == 7:
            file_name = input('\nВведите имя файла: ')
            export_json(file_name, data)
        elif choice == 8:
            file_name = input('\nВведите имя файла: ')
            export_csv(file_name, data)
        elif choice == 0:
            print_data(data)
        else:
            print('\nТакой команды не существует!')
        choice = show_menu()
