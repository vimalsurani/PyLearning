# Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.

def func_num_compare(num_list):
    print("Given List is :", num_list)
    first_num = num_list[0]
    last_num = num_list[-1]

    if first_num == last_num:
        return True
    else:
        return False


print("Result is ", func_num_compare([10, 20, 30, 0]))
print("Result is ", func_num_compare([10, 20, 30, 10]))

