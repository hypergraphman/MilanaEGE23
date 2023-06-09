f = open('26.txt')
v, n = map(int, f.readline().split())
*a, = map(int, f.readlines())
a.sort()
new_v = 0
amount = 0
for i in range(n):
    if new_v + a[i] <= v:
        new_v += a[i]
        amount += 1
        last = a[i]
print(amount)
limit = v - new_v + last
mx = 0
for el in a:
    if el <= limit and el > mx:
        mx = el
print(mx)
