import random

nums = [random.randint(-20, 20) for _ in range(10)]
print("Вихідний список:", nums)

even_nums = []
odd_nums = []
negative_nums = []
positive_nums = []

for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)
        
    if num < 0:
        negative_nums.append(num)
    elif num > 0:
        positive_nums.append(num)

print("Список парних чисел:", even_nums)
print("Список непарних чисел:", odd_nums)
print("Список від'ємних чисел:", negative_nums)
print("Список додатніх чисел:", positive_nums)