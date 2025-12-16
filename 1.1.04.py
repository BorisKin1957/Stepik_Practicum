
m, p, n = map(int, input().split())

for i in range(1, n + 1):
    m += m * p / 100
    print(f'{i}: {int(m)}')