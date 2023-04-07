from collections import Counter


def n_to_p(n, p):
    res = ''
    while n > 0:
        d = '0123456789ABCDEF'[n % p]
        res = d + res
        n //= p
    return res


# print(n_to_p(194, 5))
t = n_to_p(12 ** 34 + 7 * 12 ** 26 - 3 * 12 ** 16 + 2 * 12 ** 5 + 552, 12)
print(Counter(t))
print(set(t))
print(len(set(t)))