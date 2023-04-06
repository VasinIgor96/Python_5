
numbers = [1, 5, 2, 9, 10, 7]
k = 1

sorted_nums = sorted(numbers, reverse=True)
kth_largest = sorted_nums[k-1]

print(kth_largest)