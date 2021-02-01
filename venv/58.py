a = float(input())
b = float(input())
c = float(input())
d = 0
x = 0
x1 = 0
if a != 0:
    d = (b ** 2) - (4 * a * c)
    if d >= 0:
        x = (- b + (d ** (1 / 2))) / (2 * a)
        x1 = (- b - (d ** (1 / 2))) / (2 * a)
        if x % 1.0 == 0:
            if x == x1:
                print(int(x))
            elif x1 < x:
                print(int(x1), int(x))
            else:
                print(int(x), int(x1))
        else:
            if x == x1:
                print("{0:.6}".format(x))
            elif x1 < x:
                print("{0:.6}".format(x1), "{0:.6}".format(x))
            else:
                print("{0:.6}".format(x), "{0:.6}".format(x1))
    else:
        print()
else:
    print('"a" не должно быть равно нулю!')
