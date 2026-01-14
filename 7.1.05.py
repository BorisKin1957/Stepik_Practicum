_ = input()

numbers = list(map(int, input().split()))
new = int(input())

if new in numbers:
    print(-1)
else:
    numbers.append(new)
    print(sorted(numbers).index(new))