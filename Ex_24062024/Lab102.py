# map - return numbers
# pick 1 item and apply the function
# give the same number of elements

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def double_func(n):
    return n * 2


new_list_double = map(double_func, numbers)

# new_list_double = map(lambda n: n * 2, numbers)
print(list(new_list_double))


# Filters - function true or false
# pick item m if true keep it, false, remove it
# It can give less number of items as compared to actual
# list


def even_num(n):
    return n % 2 == 0


# new_filter_list = list(filter(even_num, numbers))
new_filter_list = list(filter(lambda x: x % 2 == 0, numbers))
print(list(filter(lambda x: x % 2 == 0, numbers)))
