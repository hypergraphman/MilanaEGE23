g = {
    'A': 'BM',
    'B': 'CM',
    'C': 'DN',
    'D': 'GE',
    'E': 'F',
    'F': '',
    'H': 'NG',
    'M': 'CNH',
    'N': 'DG',
    'T': 'AMHF',
    'G': 'EF',
}


def f(v, p):
    if 'F' == p[-1]:
        if 'C' in p or 'G' in p:
            return 1
        else:
            return 0
    # if len(p) > len(set(p)):
    #     return 0
    s = 0
    for x in g[v]:
        s += f(x, p + x)
    return s


print(f('T', 'T'))