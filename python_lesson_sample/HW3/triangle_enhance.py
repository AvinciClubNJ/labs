#!/usr/bin/env python

while True:
    userIn = input("Please enter a char between a-z to build the triangle: ")
    if len(userIn) > 0:
        c = userIn[0]
        if c >= 'a' and c <= 'z': 
            break

while True:
    widthIn = input("Please enter the triangle base width less than 20, odd number only: ")
    if len(widthIn) == 0:
        continue

    width = int(widthIn)
    if (width >= 20):
        continue

    if (width % 2 == 0):
        continue
    else:
        break

height = (width + 1) / 2

# Create triangle
for x in range (0, int(height)):
    spaceToPrint = " " * int(((width-1)/2) - x)
    charToPrint = c * int((x*2)+1)
    print(spaceToPrint, charToPrint)

print()

# Create up side down triangle
for x in range (int(height), 0, -1):
    spaceToPrint = " " * int(((width+1)/2) - x)
    charToPrint = c * int((x*2)-1)
    print(spaceToPrint, charToPrint)
