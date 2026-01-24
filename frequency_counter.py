numbers = [1, 1, 2, 3, 4, 5, 2, 1, 1, 3, 2, 4, 5]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Element frequency:")
print(frequency)