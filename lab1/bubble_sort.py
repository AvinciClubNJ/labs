# Sort list of numbers from least to greatest
numbers = [5, 4, 3, 1, 2]

for passnum in range(len(numbers) - 1, 0, -1):
    for i in range(passnum):
        if numbers[i] > numbers[i + 1]:
            temp = numbers[i]
            numbers[i] = numbers[i + 1]
            numbers[i + 1] = temp

print(numbers)