numbers = [2, 4, 6, 8, 5, 9, 1, 7, 12, 14]

numbers.append(11)
if 5 in numbers:
    numbers.remove(5)
numbers.insert(2, 8)

print(sum(numbers))
print(min(numbers))
print(max(numbers))
