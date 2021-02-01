n = int(input())
number = n % 10
if n >= 100:
    print('Введите значение < 100')
elif 10 < n < 20 or 5 <= number <= 9 or number == 0:
    print(n, 'korov', sep=' ')
elif number == 1:
    print(n, 'korova', sep=' ')
else:
    print(n, 'korovy', sep=' ')
