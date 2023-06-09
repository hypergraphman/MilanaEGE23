s = open('24_8166.txt').read()
s = s.replace('A', '!').replace('B', '!').replace('C', '!')
cur_len = 0
max_len = 0
for el in s:
    if el == '!':
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 0
print(max_len // 2)