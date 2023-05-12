s = open('24.txt').read()
s = s.replace('A', ' ').replace('B', ' ')
print(len(max(s.split())))