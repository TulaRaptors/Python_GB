def export_json(filename: str, data: list):
    json = f'{filename}.json'
    for i in data:
        s = ''
        s += f'id = {data.index(i) + 1}\n'
        for a, b in i.items():
            s += f'{a}: {b}\n'
        s += '\n'
        with open(json, 'a', encoding='utf-8') as f:
            f.write(s)


def export_csv(filename: str, data: list):
    csv = f'{filename}.csv'
    for i in data:
        s = ''
        s += f'id = {data.index(i) + 1}\n'
        for a, b in i.items():
            s += f'{a}: {b}\n'
        s += '\n'
        with open(csv, 'a', encoding='utf-8') as f:
            f.write(s)
