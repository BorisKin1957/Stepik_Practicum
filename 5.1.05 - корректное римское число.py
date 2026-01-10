'''Вам уже давалась задача на перевод римского числа в арабское. В этой задаче
вам будет так же подаваться строка(не превышающая 15 символов),
которая обозначает римское число. Но есть некоторые ограничения для перевода:

Чтобы получить ’4’ или ’9’, надо поставить ’I’ перед ’V’ или ’X’ соответственно
Чтобы получить ’40’ или ’90’, надо поставить ’X’ перед ’L’ или ’C’
Чтобы получить ’400’ или ’900’, надо поставить ’C’ перед ’D’ или ’M’
V, L, D не могут повторяться более одного раза
I, X, C, M не могут повторяться более трех раз подряд
Римская запись чисел может включать следующие символы:

’I’ — 1
’V’ — 5
’X’ — 10
’L’ — 50
’C’ — 100
’D’ — 500
’M’ — 1000
Выведите число, записанное арабскими цифрами. Если запись числа некорректная,
то выведите -1.

Sample Input 1:

VIV
Sample Output 1:

-1
Sample Input 2:

II
Sample Output 2:

2
Sample Input 3:

IIII
Sample Output 3:

-1
Sample Input 4:

MCMLXI
Sample Output 4:

1961
Sample Input 5:

IM
Sample Output 5:

-1
Sample Input 6:

MMMCMXCIX
Sample Output 6:

3999'''


def get_arabic_from_romane(s):
    # Проверка: строка не пустая и тип str
    if not s or not isinstance(s, str):
        return -1

    # Множество допустимых символов в римской записи
    valid_chars = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}

    # Проверка, что все символы в строке — допустимые
    for char in s:
        if char not in valid_chars:
            return -1

    # Порядок значений римских цифр
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    # Проверка на запрещённые повторения (например, IIII, VV и т.д.)
    invalid_repeats = [
        'IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM'
    ]
    for invalid in invalid_repeats:
        if invalid in s:
            return -1

    # Проверка: V, L, D не могут повторяться более одного раза
    if s.count('V') > 1 or s.count('L') > 1 or s.count('D') > 1:
        return -1

    # Проверка корректности вычитаемых комбинаций (например, разрешены IV, IX, но не IIX)
    valid_subtracts = {
        'I': ['V', 'X'],  # I может быть перед V и X
        'X': ['L', 'C'],  # X может быть перед L и C
        'C': ['D', 'M']  # C может быть перед D и M
    }
    # Проходим по строке
    for i in range(len(s)):
        char = s[i]
        # Проверяем, что нет трёх подряд одинаковых символов (кроме M)
        if i >= 3 and s[i] == s[i - 1] == s[i - 2] == s[i - 3] and s[i] != 'M':
            return -1

        # Проверка вычитаемых форм
        if char in valid_subtracts:
            # Если текущий символ — один из I, X, C, и за ним следует другой
            if i + 1 < len(s):
                next_char = s[i + 1]
                # Например, I может стоять перед V и X, но не перед L
                if next_char in valid_subtracts[char]:
                    # Проверим, что предыдущий символ не мешает (например, IIX — недопустимо)
                    if i > 0 and s[i - 1] == char:
                        return -1  # Например: IIX (два I перед вычитанием)
                # Если следующий символ больше, но не из разрешённого списка
                elif next_char in values and values[next_char] > values[char]:
                    return -1  # Например: IL, IC — недопустимо
        else:
            # Если символ не I, X, C, то за ним не может идти символ с большим значением
            if i + 1 < len(s):
                if values[s[i + 1]] > values[char]:
                    return -1

    # инвертируем число
    s = s[::-1]

    # вносим в итог последний символ римского числа
    result = values[s[0]]

    '''суммируем значения всех символов, учитывая, что перед «крупной» цифрой 
    меньшая вычитается, а в остальных случаях – складывается, работая с группами справа налево'''
    for i in range(len(s) - 1):
        if values[s[i]] <= values[s[i + 1]]:
            result += values[s[i + 1]]
        else:
            result -= values[s[i + 1]]

    return result


print(get_arabic_from_romane(input()))
