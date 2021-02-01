h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
if 0 <= h1 <= 24 and 0 <= m1 < 60 and 0 <= s1 < 60:
    sec1 = (h1 * 60 * 60) + (m1 * 60) + s1
else:
    print('Введите корректное время!')
if 0 <= h2 <= 24 and 0 <= m2 < 60 and 0 <= s2 < 60:
    sec2 = (h2 * 60 * 60) + (m2 * 60) + s2
else:
    print('Введите корректное время!')
print(sec2 - sec1)
