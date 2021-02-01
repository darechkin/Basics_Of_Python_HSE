def sum(a, b):
    if b != 0:
        b -= 1
        a += 1
        sum(a, b)
    else:
        print(a)


a = int(input())
b = int(input())
sum(a, b)
