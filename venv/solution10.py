number = int(input())
if 0 < number <= 10 ** 7:
    hour = number // 60 % 24
    minutes = number % 60
    print(hour, minutes, sep=' ')
else:
    print('Введите число меньше, чем 10 в 7 степени')
