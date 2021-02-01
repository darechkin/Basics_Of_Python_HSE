s = 'abcd adc abd'
pos = 0
while s.find('abc', pos) != - 1:
    print(s.find('abc', pos))
    pos = s.find('abc', pos) + 1