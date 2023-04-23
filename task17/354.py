*a, = map(int, open('17-354.txt'))
# print(a)

# mn = min(a)
mn = 10**5
for el in a:
    # str(el)[-1] == '3'
    if el < mn and abs(el) % 10 == 3:
        mn = el
sq_mn = mn**2

res = []
for i in range(len(a) - 1):
    p1 = a[i]
    p2 = a[i - 1]
    if ((abs(p1) % 10 == 3 and abs(p2) % 10 != 3 or
       abs(p1) % 10 != 3 and abs(p2) % 10 == 3) and
       p1**2 + p2**2 < sq_mn):
        res.append(p1**2 + p2**2)
print(len(res), max(res))