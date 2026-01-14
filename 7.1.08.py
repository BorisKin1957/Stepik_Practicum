_ = input()

numbers = map(int, input().split())

n = int(input())

flag = 'true'

for num in numbers:
    if num <= n:
        flag = 'false'
        break

print(flag)