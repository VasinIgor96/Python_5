
strings = ["Огірок", "Слива", "Помідор", "Салат", "Груша", "Суниця"]
prefix = "С"
result = []

for i in strings:
    if i.startswith(prefix):
        result.append(i)

print(result)