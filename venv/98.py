def merger(a, b):
    nl = []
    d = a + b
    while d:
        dn = min(d)
        while dn in d:
            nl.append(dn)
            d.remove(dn)
    return nl

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = merger(a, b)
print(c)
