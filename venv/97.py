a = [int(s) for s in input().split()]
nmin = 0
nmax = 0
for i in range(1, len(a)):
    if a[i] > a[nmax]:
        nmax = i
    if a[i] < a[nmin]:
        nmin = i
a[nmin], a[nmax] = a[nmax], a[nmin]
print(' '.join([str(i) for i in a]))
