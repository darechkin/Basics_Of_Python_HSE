x = int(input())
if x == 0:
    print('0')
else:
    y = int(input())
    a = 1
    z = 1
    if x == y:
        a += 1
        z += 1
    elif y == 0:
        print('1')
    while x != 0:
        x = int(input())
        if x == y:
            a += 1
        else:
            y = x
            a = 1
        if a >= z:
            z = a
print(z)
