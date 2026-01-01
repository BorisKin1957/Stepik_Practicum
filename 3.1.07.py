'''

Дан массив целых чисел nums, верните все тройки [nums[i], nums[j], nums[k]],
такие что i ≠ j, i ≠ k, и j ≠ k, и nums[i] + nums[j] + nums[k] == 0.

Обратите внимание, что набор решений не должен содержать повторяющихся троек.

Sample Input 1:

-1 0 1 2 -1 -4

Sample Output 1:

-1 -1 2
-1 0 1

Sample Input 2:

0 1 1

Sample Output 2:

Sample Input 3:

0 0 0

Sample Output 3:

0 0 0

'''

num = sorted(list(map(int, input().split())))
n, result = len(num), []

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if num[i] + num[j] + num[k] == 0 and [num[i], num[j], num[k]] \
                    not in result:
                result.append([num[i], num[j], num[k]])

for elem in result:
    print(*elem)
