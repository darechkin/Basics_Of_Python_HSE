def merge(A, B):
    k = []
    while len(c) != 0:
        m = min(c)
        c.remove(m)
        k.append(m)
    return k


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a + b

k = merge(a, b)
print(' '.join(map(str, k)))
