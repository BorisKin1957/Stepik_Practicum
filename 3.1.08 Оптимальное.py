def generate_parentheses(n):
    result = []

    def backtrack(current, opened, closed):
        # Базовый случай: набрано 2*n символов
        if len(current) == 2 * n:
            result.append(current)
            return
        # Можно добавить '(' если ещё не набрали n открывающих
        if opened < n:
            backtrack(current + '(', opened + 1, closed)
        # Можно добавить ')' если их меньше, чем '('
        if closed < opened:
            backtrack(current + ')', opened, closed + 1)

    backtrack('', 0, 0)
    return result


# Чтение ввода и вывод результата
n = int(input())
for combo in generate_parentheses(n):
    print(combo)

# n = int(input())
# current = []
# opened, closed = 0, 0
#
# while len(current) < 2 * n:
#     if opened < n:
#         current.append('(')
#         opened += 1
#     if closed < opened:
#         current.append(')')
#         closed += 1
# print(''.join(current))