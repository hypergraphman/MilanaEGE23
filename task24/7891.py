from string import ascii_letters, digits
line = open('24_7891.txt').read()
a = []
for s in ascii_letters + digits:
    a += [len(el) for el in line.split(s)[1:-1]]
print(max(a) + 2)
