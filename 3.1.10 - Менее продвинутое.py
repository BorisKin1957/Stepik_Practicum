'''Менее продвинутое (упрощённое) решение задачи поиска слова на доске.

Это решение использует ту же идею — перебор с возвратом (backtracking),
но с более простыми объяснениями шагов и без сложных оптимизаций.
'''




# Функция, которая проверяет, можно ли найти слово, начиная с позиции (r, c)
def word_search(r, c, pos):
    '''Функция поиска слова по доске'''
    # Если мы прошли всё слово — значит, нашли!
    if pos == len(word):
        return True

    # Проверяем, вышли ли мы за границы доски
    if r < 0 or r >= n or c < 0 or c >= m:
        return False

    # Если текущая буква на доске не совпадает с нужной из слова:
    if board[r][c] != word[pos]:
        return False

    # Если мы уже использовали эту клетку:
    if visited[r][c]:
        return False

    # Отмечаем клетку как использованную
    visited[r][c] = True

    # Пытаемся пойти в четырёх направлениях: вниз, вверх, вправо, влево
    found = False
    if word_search(r + 1, c, pos + 1):   # вниз
        found = True
    elif word_search(r - 1, c, pos + 1):  # вверх
        found = True
    elif word_search(r, c + 1, pos + 1):  # вправо
        found = True
    elif word_search(r, c - 1, pos + 1):  # влево
        found = True

    # После проверки "распосещаем" клетку (возврат)
    visited[r][c] = False

    return found


# Ввод размеров доски
n, m = map(int, input().split())

# Ввод самой доски
board = [input().split() for _ in range(n)]

# Ввод искомого слова
word = input()

# Создаём таблицу для отметки, какую клетку уже использовали
visited = [[False] * m for _ in range(n)] # изначально все клетки не посещены

# Начинаем поиск с каждой клетки доски
result = False
for row in range(n):
    for col in range(m):
        if word_search(row, col, 0):  # если слово найдено с позиции (row, col)
            result = True
            break
    if result:
        break

# Выводим результат
print(result)