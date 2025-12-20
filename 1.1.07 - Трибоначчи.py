'''

Напишите программу, которая считывает натуральное число n и выводит первые n
чисел последовательности Трибоначчи.

Примечание. Последовательность Трибоначчи – последовательность натуральных
чисел, где каждое последующее число является суммой трех предыдущих:

Sample Input 1:

10

Sample Output 1:

0 0 1 1 2 4 7 13 24 44

Sample Input 2:

1

Sample Output 2:

0

'''

def tribonachy(n, a=0, b=0, c=1):
    if n < 2:
        print(0)
    elif n == 2:
        print(1)
    else:
        print(a, b, c, end=' ')
        for i in range(3, n):
            a, b, c = b, c, a + b + c
            print(c, end=' ')

tribonachy(int(input()))