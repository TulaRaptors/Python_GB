def export_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(len(data)):
            s = f'{data[i]}'
            f.write(f'{s}\n')


def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(len(data)):
            s = f'{data[i]}'
            f.write(f'{s}\n')


def read_file(filename: str):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for i in f:
            data.append(i)
    return data


def find_contact(data: list, name: str):
    sort_data = []
    check = False
    for i in data:
        if name.lower() in i.lower():
            sort_data.append(i)
            check = True
    if not check:
        print('\nКонтакт не найден')
    return sort_data


def add_user(data: list, user_data: str):
    data.append(user_data)
