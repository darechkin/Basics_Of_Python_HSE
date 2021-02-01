import math
n = int(input())


def MinDivisor(p):
    min = 2
    while min <= math.sqrt(n):
        if n % min == 0 and min <= math.sqrt(n):
            return min
        min += 1
    return p


print(MinDivisor(n))
