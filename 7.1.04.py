_ = input()

numbers = list(map(int, input().split()))
numbers.append(int(input()))

print(*sorted(numbers))