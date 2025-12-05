'''

На вход программе подаются два натуральных числа a и b (a < b). Напишите
программу, которая находит натуральное число из отрезка [a; b] с максимальной
суммой делителей и сумму его делителей. Если таких чисел несколько, то
выведите наибольшее из них.

Программа должна вывести два числа на одной строке, разделенных пробелом:
число с максимальной суммой делителей и сумму его делителей.

Sample Input 1:

1
10

Sample Output 1:

10 18'''


number, max_sum = 0, 0

for i in range(int(input()), int(input()) + 1):
    sum_of_divisors = 0
    for j in range(1, i + 1):
        if i % j == 0:
            sum_of_divisors += j
    if sum_of_divisors > max_sum:
        max_sum = sum_of_divisors
        number = i

print(number, max_sum)
