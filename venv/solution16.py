v = int(input())
t = int(input())
if -1000 <= v <= 1000 and 0 <= t <= 1000:
    d = v * t
    print(d % 109)
else:
    print('Введите число от -1000 до 1000')
