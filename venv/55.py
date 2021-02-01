from math import floor, ceil
p = float(input())
if p > 0:
    mi = int(p)
    ma = round((p - floor(p)) * 100)
    print(mi, ma)
else:
    print('Введите число больше нуля')
