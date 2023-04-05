import random
nams = list(range(-10,20))
even_nums = []
odd_nums = []
for num in nams:
     if num %2 == 0:
         even_nums.append(num)
     else:
         odd_nums.append(num)
print("Even numbers: ",even_nums)
print("Odd numbers: ",odd_nums)