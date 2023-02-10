from view import show_menu, print_phonebook, user_contact
from model import write_csv, export_txt, read_file, add_user, find_contact


def start():
    choice = show_menu()
    phonebook = read_file('phonebook.csv')
    while (choice != '0'):
        if choice == '1':
            print_phonebook(phonebook)
        elif choice == '2':
            add_user(phonebook, user_contact())
            write_csv('phonebook.csv', phonebook)
        elif choice == '3':
            name = input('\nВведите имя для поиска: ')
            contact_list = find_contact(phonebook, name)
            print(print_phonebook(contact_list))
        elif choice == '4':
            file_name = input('\nВведите имя файла: ')
            export_txt(file_name, phonebook)
        else:
            print('\nТакой команды не существует!')
        choice = show_menu()
