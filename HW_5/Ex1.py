# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст: ")
new_text = [i for i in text.split() if 'абв' not in i]
print(f'Текст без "абв": {" ".join(new_text)}')