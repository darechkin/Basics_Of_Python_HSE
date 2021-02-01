n = int(input())
c = 1
m = 0
while n != 0:
    v = int(input())
    (n, v) = (v, n)
    if v == n:
        c += 1
    if c > m:
        m = c
    if n != v:
        c = 1
print(m)
