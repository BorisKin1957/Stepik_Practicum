'''

На вход подается слово или строка слов. Необходимо проверить, является ли
введенная строка палиндромом. Вернуть true, если строка — палиндром, и false,
если нет. Не стоит забывать про регистр букв и символ пробела.

Sample Input 1:

Hello

Sample Output 1:

False

Sample Input 2:

Was it a car or a cat I saw

Sample Output 2:

True'''

old = input().replace(' ', '').lower()
new = old[::-1]

print(old == new)