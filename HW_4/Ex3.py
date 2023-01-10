# Задача №3
# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


# sequence = ['1', '1', '3', '2', '4', '2', '2', '2', '5']
sequence = list(map(str, (input('Введите числа через пробел: ').split(' '))))
new_sequence = []
for i in sequence:
    c = sequence.count(i)
    if c == 1:
        new_sequence.append(i)
print(f'Уникальная последовательность: {new_sequence}')
