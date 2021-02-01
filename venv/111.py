def printList(lst, mySep):
    for i in range(len(lst)):
        print(lst[i], mySep, sep='', end='')
    print()
printList([1, 2, 3], 'a')
printList([5, 6, 7], 'a')