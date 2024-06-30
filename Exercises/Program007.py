# sum and average of List

# 1. Using sum() method

my_list = [6, 5, 1, 2, 5, 7, 10, 8]

# sum_list = sum(my_list)
# print(sum_list)
# avg_list = sum_list / len(my_list)
# print(avg_list)

# 2. Using Loop

count = 0

for i in my_list:
    count += i

avg = count / len(my_list)

print("Sum of list : ", count)
print("Avg of list : ", avg)
