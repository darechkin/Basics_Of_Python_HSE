s = input()
f = s.find('1')
if f != -1:
    n = s.replace('1', 'one')
    print(n)
else:
    print(s)
