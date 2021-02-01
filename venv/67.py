s = input()
f = s.find('@')
if f != -1:
    n = s.replace('@', '')
    print(n)
else:
    print(s)
