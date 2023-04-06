import random
numbers = list(range(-10,10))
def positive_numbers(numbers):
    print(numbers)
    positive_nums = []
    for num in numbers:
        if num > 0:
            positive_nums.append(num)
    return positive_nums
positive_nums_list = positive_numbers(numbers)
print(positive_nums_list)