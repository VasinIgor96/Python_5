numbers = [1, 2, 3, 2, 4, 5, 1, 6, 7, 6, 8, 9, 6, 1, 2]

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)