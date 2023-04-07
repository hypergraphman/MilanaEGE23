from itertools import product

words = list(product('АЛПЦЯ', repeat=5))
for i in range(len(words)):
    s = ''.join(words[i])
    if s == 'АППЦЦ':
        print(i + 1, s[:-1])