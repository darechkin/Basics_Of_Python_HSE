s = input()
in1 = s.find('f')
in2 = s.find('f', in1 + 1)
if (in1 == -1):
    print(-2)
else:
    if (in1 > -1 and in2 > -1):
        print(in2)
    else:
        print(-1)
