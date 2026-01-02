#print(list(range(1, 9)))

import random

tmp, result = [], []


numbers = [-1, -1, -1, -1, 1, 1, 1, 1]
for _ in range(100):
    random.shuffle(numbers)
    tmp = []
    summ = 0
    for n in numbers:
        summ += n
        if summ < 0:
            break
        else:
            continue
        if sum(numbers) == 0:
            result.append(numbers)
for element in result:
    print(*element)