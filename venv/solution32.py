a = int(input())
b = int(input())
c = int(input())
a1 = int(input())
b1 = int(input())
c1 = int(input())
(a, b, c) = (c, b, a)
if a <= b <= c and (a1 < a or b1 < a or c1 < a):
    print('The first box is larger than the second one')
elif a <= b <= c and (a1 > a or b1 > a or c1 > a):
    print('The first box is smaller than the second one')
elif a >= b >= c and (a1 < c or b1 < c or c1 < c):
    print('The first box is larger than the second one')
elif a >= b >= c and (a1 > c or b1 > c or c1 > c):
    print('The first box is smaller than the second one')

elif a <= b >= c and a == c and (a1 < a or b1 < a or c1 < a):
    print('The first box is larger than the second one')
elif a <= b >= c and a == c and (a1 > a or b1 > a or c1 < a):
    print('The first box is larger than the second one')
elif a <= b >= c and a <= c and (a1 > a or b1 > a or c1 > a):
    print('The first box is smaller than the second one')
elif a <= b >= c and a >= c and (a1 < c or b1 < c or c1 < c):
    print('The first box is larger than the second one')

elif a >= b <= c and a == c and (a1 < a or b1 < a or c1 < a):
    print('The first box is larger than the second one')
elif a >= b <= c and a >= c:
    print(b, c, a, sep=' ')
elif a >= b <= c and a <= c:
    print(b, a, c, sep=' ')
elif a >= b <= c and a == c:
    print(b, c, a, sep=' ')
elif a * b * c != a1 * b1 * c1:
    print('Boxes are incomparable')
elif a == a1 and b == b1 and c == c1:
    print('Boxes are equal')



if a * b * c == a1 * b1 * c1:
    print('Boxes are equal')
elif a * b * c > a1 * b1 * c1:
    print('The first box is larger than the second one')
elif a * b * c < a1 * b1 * c1:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
