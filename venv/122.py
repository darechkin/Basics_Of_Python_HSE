n = [int(s) for s in input().split()]
occur_before = set()
for num in n:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)
