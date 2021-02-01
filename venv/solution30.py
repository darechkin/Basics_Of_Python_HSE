a = int(input())
b = int(input())
c = int(input())
(a, b, c) = (c, b, a)
if a == b == c:
    print('3')
elif a != b == c or a == b != c or a == c != b:
    print('2')
elif a != b != c:
    print('0')
