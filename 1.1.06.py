numbers = map(int, input().split())

#result = [num ** 2 for num in numbers if num % 2 == 0 and str(num ** 2)[-1]
#                                                              != '4']
result = [n for num in numbers if num % 2 == 0 and str(n := num ** 2)[
    -1]!= '4']

print(*result)