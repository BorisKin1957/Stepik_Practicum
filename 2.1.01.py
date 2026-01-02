'''

На вход подается количество чисел, n-ое количество целых чисел и искомое число.
Необходимо найти подмассив из двух элементов, сумма которых будет равна искомому числу.

Sample Input 1:

4
2 7 11 15
9

Sample Output 1:

[0, 1]'''

n1 = int(input())
numbers = list(map(int, input().split()))
n2 = int(input())

result = []

for i in range(n1):
    for j in range(i + 1, n1):  # j > i
        if numbers[i] + numbers[j] == n2:
            result = [i, j]
            break
    if result: # прерывание цикла при подмассиве из 2х элементов
        break

print(result)