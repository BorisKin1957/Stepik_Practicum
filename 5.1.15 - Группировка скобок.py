def generate_psp(n):
    results = []
    max_pairs = n // 2

    def dfs(curr, stack):
        if len(curr) == n:
            if not stack:
                results.append(curr)
            return

        # Правильный лексикографический порядок: '(', ')', '[', ']'

        # 1. Попробуем '('
        if curr.count('(') < max_pairs and stack.count('[') == 0:
            dfs(curr + '(', stack + ['('])

        # 2. Попробуем ')'
        if stack and stack[-1] == '(':
            dfs(curr + ')', stack[:-1])

        # 3. Попробуем '['
        if curr.count('[') < max_pairs:
            dfs(curr + '[', stack + ['['])

        # 4. Попробуем ']'
        if stack and stack[-1] == '[':
            dfs(curr + ']', stack[:-1])

    dfs('', [])
    return results


# Чтение входа
n = int(input().strip())

# Генерация и вывод
sequences = generate_psp(n)
for seq in sequences:
    print(seq)
