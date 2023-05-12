s = open('24_gen.txt').read()

k = 0
for i in range(2, len(s)):
    c1, c2, c3 = s[i - 2], s[i - 1], s[i]
    if c1 in 'BCD' and c2 in 'BDE' and c1 != c2 and c3 in 'BCE' and c2 != c3:
        k += 1
print(k)