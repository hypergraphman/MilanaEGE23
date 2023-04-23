# *a, = map(int, open('17-354.txt'))
a = [int(el) for el in open('17-354.txt')]
mx = -10 ** 5
for el in a:
    if el > mx and abs(el) % 10 == 5:
        mx = el
sq_mx = mx ** 2
res = []
for i in range(len(a) - 1):
    p1, p2 = a[i], a[i - 1]
    if ((abs(p1) % 10 == 8 and abs(p2) % 10 != 8 or
       abs(p1) % 10 != 8 and abs(p2) % 10 == 8) and
       p1 ** 2 + p2 ** 2 > sq_mx):
        res.append(p1 ** 2 + p2 ** 2)
print(len(res), min(res))
