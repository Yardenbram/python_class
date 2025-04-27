my_set = {1, 2, 3, 4, 5}
tuple_squares = tuple(x**2 for x in my_set)

sorted_list = sorted(my_set, reverse=True)
intersection = my_set & set(tuple_squares)

print(sorted_list)
print(len(tuple_squares))
print(len(my_set))

try:
    tuple_squares[0] = 0
except TypeError as e:
    print(e)

print(intersection)
