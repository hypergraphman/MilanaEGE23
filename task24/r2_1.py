s = open('24.txt').read()
for c in 'DEFGHI...':
    s = s.replace(c, ' ')
print(len(max(s.split())))