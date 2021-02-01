a = int(input())
b = int(input())
if 1 <= a <= 1000 and 1 <= b <= 1000:
    if a > b:
        print(a)
    else:
        print(b)
else:
    print('Введите целое число от 1 до 1000')
