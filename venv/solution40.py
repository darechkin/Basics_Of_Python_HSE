n = int(input())
c = 0
if n >= 0:
    while n != 0:
        c += 1
        n = int(input())
    print(c)
else:
    print('Введите положительное число')
