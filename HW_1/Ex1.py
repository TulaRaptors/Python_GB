# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_of_week = int(input('Введите день недели: '))
weekdays = [1, 2, 3, 4, 5]
weekends = [6, 7]
if day_of_week in weekdays:
    print('Будний день')
elif day_of_week in weekends:
    print('Выходной')
else:
    print('Неверный номер!')