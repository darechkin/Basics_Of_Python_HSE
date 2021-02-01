n = int(input())
m = n
c = 1
while n != 0:
    n = int(input())
    if n > m:
        m = n
        c = 1
    elif n == m:
        c += 1
print(c)
