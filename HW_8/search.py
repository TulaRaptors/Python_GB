def find_employee(data: list, sort: str, field: str):
    sort_data = []
    for i in data:
        if i.get(field).lower() == sort.lower():
            sort_data.append(i)
    return sort_data


def find_choice():
    print('1 - Поиск по имени\n'
          '2 - Поиск по фамилии')
    choice = int(input('Введите вариант поиска: '))
    if choice == 1:
        return 'Имя'
    elif choice == 2:
        return 'Фамилия'


def find_by_id(data: list, id: int):
    sort_data = []
    sort_data.append(data[id - 1])
    return sort_data
