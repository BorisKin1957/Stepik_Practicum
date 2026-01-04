from itertools import combinations
'''Функция combinations() возвращает итератор, который содержит все сочетания из 
элементов переданного итерируемого объекта. Каждое сочетание заключено в кортеж 
нужной длины n.'''

def get_good_brackets(n):
    result = []
    indices = list(range(2 * n))  # позиции от 0 до 2n-1

    # выбираем n позиций для '('
    for open_positions in combinations(indices, n):
        tmp = []
        balance = 0
        for i in range(2 * n):
            if i in open_positions:
                tmp.append('(')
                balance += 1
            else:
                tmp.append(')')
                balance -= 1
            if balance < 0:
                break
        else:  # если не было отрицательного баланса
            result.append(''.join(tmp))
    return result


n = int(input())
for combo in get_good_brackets(n):
    print(combo)