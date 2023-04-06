
numbers = [1, 5, 2, 9, 10, 7, 8, 6]
i = sum(numbers) / len(numbers)
count = 0

for num in numbers:
    if num > i:
        count += 1

print(count)