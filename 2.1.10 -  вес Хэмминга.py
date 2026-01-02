'''

Напишите функцию, которая принимает двоичное представление положительного
целого числа и возвращает количество установленных битов (также известное как вес Хэмминга).

Sample Input 1:

11

Sample Output 1:

3

Sample Input 2:

128

Sample Output 2:

1

Sample Input 3:

2147483645

Sample Output 3:

30

'''


def get_hamming_weight(n: int, result=0) -> int:
    # делим циклически число на 2, остатки от деления суммируем
    while n > 0:
        result += n % 2
        n = n // 2
    return result

print(get_hamming_weight(int(input())))
