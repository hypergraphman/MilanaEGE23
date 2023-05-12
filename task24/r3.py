s = open('24.txt').read()

cur_len = 0
max_len = 0
temp = 'EAB'
for el in s:
    if el == temp[cur_len % len(temp)]:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    elif el == temp[0]:
        cur_len = 1
    else:
        cur_len = 0
print(max_len)