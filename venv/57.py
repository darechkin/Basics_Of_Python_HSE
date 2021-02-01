from math import floor, ceil
p = float(input())  # процентов годовых
x = int(input())  # рублей
y = int(input())  # копеек
xk = x * 100  # рубли в копейках
v = 0  # вклад в копейках
vr = 0  # величина вклада рублей
vk = 0  # величина вклада копеек
if p >= 0 and x >= 0 and y >= 0:
    v = (xk + y) * (1 + (p / 100))
    vr = v // 100
    vk = (v % 100) * 1.0001
    print(round(vr), int(vk))
else:
    print('Введите положительное значение')
