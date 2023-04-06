import random
numbers = list(range(10,20))
min_num = numbers[0]
max_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num
    elif num > max_num:
        max_num = num

min_index = numbers.index(min_num)
max_index = numbers.index(max_num)

numbers[min_index] = max_num
numbers[max_index] = min_num

print(numbers)