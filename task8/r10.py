from itertools import permutations

words = permutations('KAPKAN')
s = set()
for w in words:
    word = ''.join(w)
    if 'KK' not in word and 'AA' not in word:
        s.add(word)
print(len(s))