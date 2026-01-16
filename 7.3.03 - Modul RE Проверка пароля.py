import sys
import re

# Компилируем регулярные выражения для повышения производительности
has_upper = re.compile(r'[A-Z]')        # хотя бы одна заглавная латинская
has_lower = re.compile(r'[a-z]')        # хотя бы одна строчная латинская
has_digit = re.compile(r'\d')           # хотя бы одна цифра
has_symbol = re.compile(r'[!@#$%^&*()\-_+=]')  # спецсимвол (минус экранирован)

for line in sys.stdin:
    password = line.strip()

    # Проверяем длину
    if not (8 <= len(password) <= 20):
        print('INVALID')
        continue

    # Проверяем все условия через регулярные выражения
    if (has_upper.search(password) and
        has_lower.search(password) and
        has_digit.search(password) and
        has_symbol.search(password)):
        print('VALID')
    else:
        print('INVALID')