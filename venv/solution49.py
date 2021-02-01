n = int(input())
nn = n
c = 1
m = 1
while n != 0:
    n = int(input())
    if n == nn:
        c += 1
        m = c
    else:
        c = 1
    if n == 0:
        continue
print(c)
