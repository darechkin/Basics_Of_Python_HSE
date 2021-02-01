a, b, c, d, e = int(input()), int(input()), int(input()), int(input())
(a, b, c) = (c, b, a)
if a <= b <= c:
    print(a, b, c, sep=' ')
elif a >= b >= c:
    print(c, b, a, sep=' ')
elif a <= b >= c and a == c:
    print(a, c, b, sep=' ')
elif a <= b >= c and a <= c:
    print(a, c, b, sep=' ')
elif a <= b >= c and a >= c:
    print(c, a, b, sep=' ')
elif a >= b <= c and a == c:
    print(b, c, a, sep=' ')
elif a >= b <= c and a >= c:
    print(b, c, a, sep=' ')
elif a >= b <= c and a <= c:
    print(b, a, c, sep=' ')
elif a >= b <= c and a == c:
    print(b, c, a, sep=' ')
