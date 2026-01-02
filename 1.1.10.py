h = int(input())

n = h // 2 + 1

print(*[i * '*' for i in range(1, n + 1)], sep='\n')
print(*[i * '*' for i in range(n - 1, 0, -1)], sep='\n')