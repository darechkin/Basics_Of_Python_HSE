s = input()
pos = s.find('f')
pos1 = s.rfind('f')
if pos == -1:
    print()
elif pos == pos1:
    print(pos)
else:
    print(pos, pos1)
