g = {
    'A': 'BED',
    'B': 'V',
    'V': 'ZGY',
    'Y': 'ZL',
    'L': 'K',
    'K': 'Z',
    'Z': 'GL',
    'G': 'AB',
    'E': 'ZD',
    'I': 'ZEK',
    'D': 'I'
}


def f(v, p):
    if len(p) > 1 and p[0] == p[-1]:
        print(p)
        return 1
    if len(p) > len(set(p)):
        return 0
    return sum(f(x, p + x) for x in g[v])


print(f('G', 'G'))