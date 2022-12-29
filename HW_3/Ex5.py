# Задача №5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):
    if n == 0:
        return 0
    elif n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input('Введите число: '))
fib = []
for i in range(-n, n + 1):
    if i < 0:
        fib.append((-1) ** (-i + 1) * fibonacci(-i))
    else:
        fib.append(fibonacci(i))
print(fib)
