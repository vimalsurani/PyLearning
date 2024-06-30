# Reversing a List

# 1. Using the Reversed() and Reverse() Built-In Function

my_list = [4, 5, 6, 7, 8, 9]

# my_list.reverse()
# print(my_list)

# my_list1 = list(reversed(my_list))
# print(my_list1)


# 2. Using Slicing

# def reverse():
#     new_list = my_list[::-1]
#     return new_list
#
#
# print(reverse())

# 3.Using the insert() Function

# lst = []
#
# for i in my_list:
#     lst.insert(0, i)
#
# print(lst)

# 4. Using List Comprehension

new_list = [my_list[len(my_list) - i]
            for i in range(1, len(my_list) + 1)]
print(new_list)
