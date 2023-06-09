s = open('24_2498.txt').read()

k = 0
for i in range(len(s) - 2):
    if s[i] + s[i + 1] + s[i + 2] == 'XIX':
        k += 1
print(k)