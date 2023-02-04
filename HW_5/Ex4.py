# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def encode(t):
    count = 1
    result = ''
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            count += 1
        else:
            result = result + str(count) + t[i]
            count = 1
    if count > 1 or (text[len(t) - 2] != t[-1]):
        result = result + str(count) + t[-1]
    return result


def decode(t):
    number = ''
    result = ''
    for i in range(len(t)):
        if not t[i].isalpha():
            number += t[i]
        else:
            result = result + t[i] * int(number)
            number = ''
    return result


with open('file.txt', 'w') as data:
    data.write('aaaaaaaaaabbbbcccccccccccccccccc')

with open('file.txt', 'r') as data:
    text = data.readline()

with open('encoded_file.txt', 'w') as data:
    data.write(encode(text))

with open('encoded_file.txt', 'r') as data:
    code = data.readline()

with open('decoded_file.txt', 'w') as data:
    data.write(decode(code))
