class Man:
    name = ''
    family = ''
    school = 0
    bal = 0

n = input()
peopleList = []

inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
for line in lines:
    k = list(map(str, line.split()))
    line.split(' ')
    print(line, end='', sep='')
    print(line, file=outFile, sep='', end='')
print(lines[1])
print(k)
