'''

На вход подаётся число n, n-ое количество целочисленных элементов и искомый
элемент. Необходимо удалить все вхождения этого элемента и вернуть оставшееся
количество элементов.

Sample Input 1:

5
1 2 2 3 2
2

Sample Output 1:

2

Sample Input 2:

4
1 2 3 4
5

Sample Output 2:

4

Sample Input 3:

5
5 4 3 3 3
3

Sample Output 3:

2

'''


_ = int(input()) # излишнее данное
numbers = map(int, input().split())
sample = int(input())

# обходим numbers, если видим число не равное sample, вносим 1 в список.
# Выводим сумму списка

print(sum([1 if num != sample else 0 for num in numbers]))