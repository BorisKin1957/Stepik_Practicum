
import re

result = re.fullmatch(r'[^@]+@[^@\.]+\.[^@]+', input())

print(bool(result))

# import re
# a = input()
# b=re.fullmatch(r'\w+@\w+\.\w+', a)
# print(bool(b))