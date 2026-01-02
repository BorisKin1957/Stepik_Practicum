#print(input()[:-1].count(input()))
new = input()
sym = input()

while new[-1] == sym:
    new = new[:-1]

while new[0] == sym:
    new = new[1:]

while sym * 2 in new:
    new = new.replace(sym * 2, sym)

print(new.count(sym) + 1)