n = int(input())
if n > 0:
    s = n % 60
    m = n // 60
    h = m // 60
    h1 = h % 24
    m1 = m % 60
    if s < 10 or m1 < 10:
        print(print(h1, ':', '0', m1, ':', '0', s, sep=''))
    else:
        print(print(h1, ':', m1, ':', s, sep=''))
else:
    print('Введите положительное число!')
