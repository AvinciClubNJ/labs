# Find the maximum number from a list of numbers

numbers = [1, -20, 0, 100, -5, 4, 10, 23, -19, 99]

max_num = numbers[0]

for i in numbers[1:]:
    if i > max_num:
        max_num = i

print("Maximum number in the list ", numbers, "is", max_num )