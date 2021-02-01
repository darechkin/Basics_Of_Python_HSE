n = int(input())
c = 0
while n > 0 or n < 0 and n != 0:
    if n % 2 == 0:
        c += 1
    elif n == 0:
        c += 0
    n = int(input())
print(c)
