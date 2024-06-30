# How To Find the Length of a List


my_list = [10, 20, 30, 40, 50,60]


# 1. Using len()

# print(len(my_list))


# 2. Using loop

# Printing test_list
# print("The list is : " + str(my_list))

# Initializing counter
# count = 0
#
# for i in my_list:
#     # incrementing counter
#
#     count = count + 1
#
# # Printing length of list
# print("Length of list using loop : " + str(count))


# 3.Using Recursion


def list_len_func(my_list):
    # Base case: if the list is empty, return 0
    if not my_list:
        return 0
    # Recursive case: add 1 to the count of the remaining elements in the list
    return 1 + list_len_func(my_list[1:])


print("The length of the list is:", list_len_func(my_list))
