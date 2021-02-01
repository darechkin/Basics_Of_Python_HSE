n = int(input())
i = 1
print(i)
while i != n:
    print(*tuple(range(1, i + 2)), sep='')
    i = i + 1
