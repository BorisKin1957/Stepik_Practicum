'''

На вход подаётся строка, соответствующая римскому числу. Необходимо написать
программу, которая будет переводить римское число в арабское.

Значения римских чисел: [I - 1], [V - 5], [X - 10], [L - 50], [C - 100], [D - 500], [M - 1000].

Sample Input 1:

VII

Sample Output 1:

7

Sample Input 2:

I

Sample Output 2:

1

Sample Input 3:

IX

Sample Output 3:

9

Sample Input 4:

MCDL

Sample Output 4:

1450

'''


rom_dict =  {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# вводим число и инвертируем его
rom_word = list(input()[::-1])

# вносим в итог последний символ римского числа
result = rom_dict[rom_word[0]]

'''суммируем значения всех символов, учитывая, что перед «крупной» цифрой 
меньшая вычитается, а в остальных случаях – складывается, работая с группами справа налево'''
for i in range(len(rom_word) - 1):
    if rom_dict[rom_word[i]] <= rom_dict[rom_word[i + 1]]:
        result += rom_dict[rom_word[i + 1]]
    else:
        result -= rom_dict[rom_word[i + 1]]

print(result)