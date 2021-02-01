a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
(a, b, c) = (c, b, a)
if d < a or d < c or d < b:
    print('NO')
elif e < a or e < c or e < b:
    print('NO')
else:
    print('YES')
