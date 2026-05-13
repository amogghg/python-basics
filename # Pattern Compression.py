# Pattern Compression

numbers = [1, 1, 1, 2, 2, 3, 3, 3]

result = []

count = 1

for i in range(len(numbers) - 1):

    if numbers[i] == numbers[i + 1]:
        count += 1

    else:
        result.append((numbers[i], count))
        count = 1

result.append((numbers[-1], count))

print("Compressed Output:", result)