a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a <= b <= c and d * e >= a * b:
    print('YES')
elif a >= b >= c and d * e >= c * d:
    print('YES')
elif a <= b >= c and a == c and d * e >= a * c:
    print('YES')
elif a <= b >= c and a <= c and d * e >= a * c:
    print('YES')
elif a <= b >= c and a >= c and d * e >= a * c:
    print('YES')
elif a >= b <= c and a == c and d * e >= b * c:
    print('YES')
elif a >= b <= c and a >= c and d * e >= b * c:
    print('YES')
elif a >= b <= c and a <= c and d * e >= b * a:
    print('NO')
elif a >= b <= c and a == c and d * e >= b * c:
    print('YES')
else:
    print('NO')
