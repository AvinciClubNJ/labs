#!/usr/bin/env python

mylist = list(range(100, 201))
#mylist = list(range(12, 401))

newlist = []
for numberToCheck in mylist:
    removeit = False
    y = 2
    divideList = list(range(2, numberToCheck))
    for y in divideList:
        if numberToCheck % y == 0:
            removeit = True
            break
    if removeit == False:
        newlist.append(numberToCheck)

print("number of prime numbers between 100 - 200: ", len(newlist))
print(newlist)
