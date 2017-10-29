#!/usr/bin/env python3

mysum = 0

def get_sum(start, end):
    sum1 = 0
    for i in range(start, end+1):
        sum1 = sum1 +i
    return sum1

index = 0
while index < 3:
    startNum = int(input("Enter start: "))
    endNum = int(input("Enter end: "))
    mysum = get_sum(startNum, endNum)
    print ("sum of numbers between ", startNum, " to ", endNum, ": ", mysum, ". ")
    index += 1
