# Python program to interchange first and last elements in a list

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

my_list = [12, 35, 9, 56, 24]

# 1: Using length of the list and simply swap the first element with (n-1)th element.

# Swap function
# def swap_ele():
#     size = len(my_list)  # 5
#     # Swapping
#     temp = my_list[0]  # 12
#     my_list[0] = my_list[size - 1]  # 12 = 24
#     my_list[size - 1] = temp  # 24 = 12
#
#     return my_list

# 2: Using referred as my_list[-1] - swap my_list[0] with my_list[-1]

# print(swap_ele())

# def swap_ele():
#     my_list[0], my_list[-1] = my_list[-1], my_list[0]   # 12,24 = 24 ,12
#
#     return my_list
#
#
# print(swap_ele())


# 3: Using tuple variable - say get, and unpack

# def swap_ele(list1):
#     # Storing the first and last element
#     # as a pair in a tuple variable get
#     get = my_list[0], my_list[-1]  # 12 , 24
#
#     my_list[-1], my_list[0] = get
#     # unpacking those elements
#     return list1


# print(swap_ele(my_list))


# 4: Using * operand

# def swap_ele(my_list1):
#     start, *middle, end = my_list1
#     my_list1 = [end, *middle, start]
#
#     return my_list1
#
#
# print(swap_ele(my_list))

# 5: use the inbuilt function list.pop()

# def swap_func(my_list1):
#     first = my_list1.pop(0)
#     last = my_list1.pop(-1)
#     print(first)
#     print(last)
#
#     my_list1.insert(0, last)
#     my_list1.insert(4, first)
#
#     return my_list1
#
#
# print(swap_func(my_list))

# 6: Using slicing
def swap_func(my_list1):
    # Check if list has at least 2 elements
    if len(my_list1) >= 2:
        # Swap the first and last elements using slicing
        my_list1 = my_list1[-1:] + my_list1[1:-1] + my_list1[:1]
    return my_list1


# Printing the original input
print("The original input is:", my_list)

result = swap_func(my_list)

# Printing the result
print("The output after swap first and last is:", result)
