xn = 0
xn1 = 0
n = -1
n1 = -1
while n != 0 or n1 != 0:
    n = int(input())
    if n == 0:
        break
    elif n == n1:
        xn1 += 1
    elif n > n1:
        xn = 0
        xn1 += 1
    elif n < n1:
        xn1 = xn1
    n1 = int(input())
    if n1 == 0:
        break
    elif n1 == n:
        xn1 += 1
    elif n1 > n:
        xn += 1
        xn1 = 0
    elif n1 < n:
        xn1 = xn1
(xn, xn1) = (xn1, xn)
print(xn)
print(xn1)
