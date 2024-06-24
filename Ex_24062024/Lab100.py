# Filter in Python
# filter() is a built-in function
# It allows you to filter elements in the list, tuple, set.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Filter on the above -> even ->
# new_list_Even = [2, 4, 6, 8, 10]


def check_num_even(num):
    return num % 2 == 0


def greater_5(num):
    return num > 5


new_numbers_even = filter(check_num_even, numbers)
print(list(new_numbers_even))
new_numbers_five = filter(greater_5, numbers)
print(list(new_numbers_five))
