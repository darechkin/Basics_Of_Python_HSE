def umn(a, n):
    c = a ** n
    if a % 2 == 0:
        c = (a ** 2) ** (n / 2)
    else:
        c = a * a ** (n - 1)
    return c

a = float(input())
n = float(input())
umn(a, n)
print(float(umn(a, n)))
