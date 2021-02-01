def power(a, n):
    k = a * a ** (n - 1)
    return k


a = float(input())
n = int(input())

print(power(a, n))
