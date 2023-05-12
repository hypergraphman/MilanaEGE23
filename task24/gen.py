import random

s = ''
for _ in range(10**5):
    s += random.choice('ABCDE')

f = open('24_gen.txt', 'w')
f.write(s)