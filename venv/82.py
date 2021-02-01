a = int(input())
b = int(input())
c = range(a, b + 1)
if a <= b:
    print(*tuple(c))
else:
    print('A должно быть меньше B!')
