# Check if element exists in list
# my_list = [1, 6, 3, 5, 4]
# 3  # Check if 3 exist or not.
# Output: True
# Explanation: The output is True because the element we are looking is exist in the list.

my_list = [1, 6, 3, 5, 4]

# 1. Using “in” statement
i = 3


# if i in my_list:
#     print("Exists in list")
# else:
#     print('Not exists in list')

# 2. Using loop
#
# for i in my_list:
#     if i == 3:
#         print("Exists in list")

# 3. Using count() method

# exist_count = my_list.count(3)
#
# if exist_count > 0:
#     print("Exists in list")
# else:
#     print("Not exists in list")

# 4. Using find() method

# x = list(map(str, my_list))
# y = "-".join(x)
#
# if y.find("9") != -1:
#     print("Exists in list")
# else:
#     print("Not exists in list")

# 5.Using filter() Function

# element_to_check = 9
#
# filtered_elements = filter(lambda x: x == element_to_check, my_list)
#
# if list(filtered_elements):
#     print("Exists in list")
# else:
#     print("Not exists in list")

def myFunc(x):
    if x != 5:
        return False
    else:
        return True


filtered_elements = filter(myFunc, my_list)

if list(filtered_elements):
    print("Exists in list")
else:
    print("Not exists in list")
