from itertools import product

words = product('0123456', repeat=6)
k = 0
for w in words:
    s = ''.join(w)
    if s[0] != '0' and s.count('6') == 1:
        q = s.replace('2', '6').replace('4', '6').replace('0', '6').replace('1', '5').replace('3', '5')
        if '55' not in q and '66' not in q:
            k += 1
print(k)
