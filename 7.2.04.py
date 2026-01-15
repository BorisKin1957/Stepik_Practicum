words = input().split()

result = [word for word in words if word in ('false', 'true')]

if result:
    print(*result)
else:
    print('Empty')