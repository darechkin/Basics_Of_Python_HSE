k = int(input())
if k <= 10 ** 5:
    N = []
    i = 0
    while i < k:
        x = int(input())
        if abs(x) <= 10 ** 9:
            N.append(x)
            i += 1

    print(*sorted(N))
