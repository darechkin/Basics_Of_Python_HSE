n = int(input())
if 0 <= n <= 1000:
    n1 = str(n) * 100
    print(int(n1) ** 2)
else:
    print('Введите число от 0 до 1000')
