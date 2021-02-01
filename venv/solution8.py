abc = int(input())
if 100 <= abc <= 999:
    c = abc % 10
    c1 = abc // 10
    b = c1 % 10
    b1 = c1 // 10
    a = b1 % 10
    print(c + b + a)
else:
    print('Неправильный ответ')
