c = 0
c1 = 0
m = 0
n = -1
n1 = -1
while n != 0 or n1 != 0:
    n = int(input())
    if n == 0:
        break
    if n == n1:
        c += 1
    elif n != n1:
        c1 += 1
        if c >= m:
            с = m
        else:
            c = 0
    n1 = int(input())
    if n1 == 0:
        break
    if n1 == n:
        c += 1
    elif n1 != n:
        c1 += 1
        if c >= m:
            c = m
        else:
            c1 = 0
print(m)