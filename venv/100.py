def merge(A, B):
    c = a + b
    k = []
    for i in range(len(c)):
        m = min(c)
        k.append(m)
        c.remove(m)
    return k


a = list(map(int, input().split()))
b = list(map(int, input().split()))

k = merge(a, b)
print(' '.join(map(str, k)))
