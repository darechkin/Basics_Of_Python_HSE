n = int(input())
k = int(input())
if 1 <= n <= 10000 and 1 <= k <= 10000:
    print(int(k // n))
else:
    print('Укажите число от 1 до 10 000')

