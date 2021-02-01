n = int(input())
i = 0
p = 0
while i < n:
    if i < n:
        i += 1
        p += (1 / (i ** 2))
    elif i == n:
        i = i
        p += (1 / (i ** 2))
print(float(p))
