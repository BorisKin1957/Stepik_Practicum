
_ = input()

numbers = map(int, input().split())

flag = 'true'

for num in numbers:
    if num % 2 == 0 or num < 0:
        flag = 'false'
        break

print(flag)

