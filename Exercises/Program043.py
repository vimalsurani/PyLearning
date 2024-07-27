# Print list in reverse order using a loop


list1 = [10, 20, 30, 40, 50]

# new_list = reversed(list1)
# for i in new_list:
#     print(i)


size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])
