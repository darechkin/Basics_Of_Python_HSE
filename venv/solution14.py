n = int(input())
if 0 <= n <= 1000:
    if n % 2 == 0:
        print(n + 2)
    else:
        print(n + 1)
else:
    print('Введите число от 0 до 1000')