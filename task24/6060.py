s = open('24_6060.txt').read()

k = 0
for i in range(len(s) - 8):
    if s[i] == s[i + 8] and s[i + 1] == s[i + 7] and s[i + 2] == s[i + 6] and s[i + 3] == s[i + 5]:
        k += 1
print(k)