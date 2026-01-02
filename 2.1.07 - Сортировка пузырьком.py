'''
На вход подаётся количество элементов и n-ое количество целочисленных элементов.
Самостоятельно реализуйте метод пузырьковой сортировки. В ответ выводить
отсортированный массив элементов. Элементы в ответе должны идти через пробел.
Если массив пустой или введён отрицательный размер массива, то вывести Empty Result.

Sample Input 1:

6
-2 4 0 6 1 7

Sample Output 1:

-2 0 1 4 6 7

Sample Input 2:

0

Sample Output 2:

Empty Result

Sample Input 3:

-1

Sample Output 3:

Empty Result

'''

n = int(input())

if n > 0:
    numbers = list(map(int, input().split()))
    tmp = []
    while tmp != numbers: # повторяем сортировку, пока список numbers меняется
        tmp = numbers[:] # Копия списка numbers
        # сравниваем соседние числа списка и меняем местами, если левое больше
        # правого
        for i in range (n - 1):
            a = numbers[i]
            b = numbers[i + 1]
            if a > b: #
                numbers[i] = b
                numbers[i + 1] = a
    print(*numbers)
else:
    print('Empty Result')