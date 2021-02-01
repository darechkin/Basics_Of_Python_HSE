def IsPrime(n):
    i = 2
    j = 0
    while True:
        if(i*i <= n and j != 1):
            if n % i == 0:
                j = j + 1
            i = i + 1
        elif j == 1:
            return False
        else:
            return True


n = float(input())
if IsPrime(n) is True:
    print('YES')
else:
    print('NO')
