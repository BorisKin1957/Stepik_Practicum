'''Дан массив символов размером m x n (доска) и строка (слово), верните true,
если слово существует в сетке.

Слово может быть построено из букв последовательно соседних ячеек, где соседние
ячейки являются горизонтально или вертикально соседними. Одна и та же ячейка с буквой не может быть использована более одного раза.

Sample Input 1:

3 4
A B C E
S F C S
A D E E
ABCCED
Sample Output 1:

True'''


def exist(board, word):
    if not board or not board[0] or not word:
        return False

    rows, cols = len(board), len(board[0])

    # Функция DFS для поиска слова по доске
    def dfs(r, c, index):
        # Если прошли всё слово — нашли
        if index == len(word):
            return True
        # Проверяем границы, соответствие буквы и посещение
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != word[index] or visited[r][c]):
            return False

        # Отмечаем ячейку как посещённую
        visited[r][c] = True
        # Попробуем все 4 направления: вверх, вниз, влево, вправо
        found = (dfs(r + 1, c, index + 1) or
                 dfs(r - 1, c, index + 1) or
                 dfs(r, c + 1, index + 1) or
                 dfs(r, c - 1, index + 1))
        # Откат изменений
        visited[r][c] = False
        return found

    # Матрица для отслеживания посещённых ячеек
    visited = [[False] * len(board[0]) for _ in range(len(board))]

    # Попробуем начать с каждой ячейки
    for r in range(len(board)):
        for c in range(len(board[0])):
            if dfs(r, c, 0):  # Если нашли слово — возвращаем True
                return True
    return False


# Ввод данных
n, m = map(int, input().split())
matrix = [input().split() for _ in range(n)]
word = input()

# Проверка и вывод результата
result = exist(matrix, word)
print(result)