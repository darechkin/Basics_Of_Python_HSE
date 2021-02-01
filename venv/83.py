a = int(input())
b = int(input())
if a < b:
    print(*tuple(range(a, b + 1)))
elif a > b:
    print(*tuple(range(a, b - 1, -1)))
else:
    print(a)
