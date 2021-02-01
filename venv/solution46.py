c = 0
c1 = 0
n = int(input())
if n == 0:
    c = 0
else:
    c = 1
n1 = int(input())
if n1 == 0:
    с1 = 0
elif n1 == n:
    c += 1
elif n1 != n:
    c1 += 1
while n != 0 or n1 != 0:
    n = int(input())
    if n == 0:
        print(c)
    elif n != n1:
        c = 1
    elif n == n1:
        c += 1
    n1 = int(input())
    if n1 == 0:
        print(c1)
    elif n1 == n:
        c += 1
    elif n1 != n:
        c1 += 1
print(c)
