n = map(int, input().split())
for num in n:
    if num % 2 == 0:
        print(' '.join([str(num)]), end=' ')
