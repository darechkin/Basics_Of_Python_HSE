from math import floor, ceil
n = float(input())
m = n - int(n)
x = 0
if m >= 0.5:
    x = ceil(n)
else:
    x = floor(n)
print(x)
