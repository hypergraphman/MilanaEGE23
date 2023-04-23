*a, = map(int, open('temp.txt'))
print(a)

# mn = min(a)
mn = float('inf')
for el in a:
    if el < mn:
        mn = el

res = []
for i in range(1, len(a)):
    p1, p2 = a[i - 1], a[i]
    if p1 % mn == 0 or p2 % mn == 0:
        res.append(p1 + p2)
print(len(res), max(res))