# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2])
# для всех значений предикат.


def truth_search(x):
    if not (x[0] or x[1] or x[2]) == (not x[0] and not x[1] and not x[2]):
        return 1
    else:
        return 0


print('Таблица истинности:')
print('X Y Z')
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(f'{i} {j} {k} = {truth_search([i, j, k])}')
