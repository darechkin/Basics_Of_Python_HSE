n = 1
m = 0
m2 = m
while n != 0:
    n = int(input())
    if n >= m:
        m2 = m
        m = n
    elif m2 < n < m:
        m2 = n
if m2 == m:
    print(m)
else:
    print(m2)
