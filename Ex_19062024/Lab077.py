# List - Collection of Items (Duplicate Allowed)

my_list1 = [1, 2, 3]
my_list2 = [1, "Vimal", 15.35]

# Indexing
print("Element at index 0 :", my_list1[0])

# Changing an element
my_list1[1] = 10
print("List after changing element index 1 :", my_list1)

# append()

my_list1.append(5)
print("List after appending:", my_list1)

# extend()
my_list1.extend([7, 8])
print("List after extending:", my_list1)

# insert()
my_list1.insert(1, 100)
print("List after inserting '100' at index 1:", my_list1)

# remove()

my_list1.remove(100)
print("List after removing 100 ;", my_list1)

my_copy_list = my_list1.copy()
print(my_copy_list)

# clear
my_list1.clear()
print("Initial llist:", my_list1)
print("Copy List:", my_copy_list)

# print("Index of 3 in the list:", my_list1.index(3))  # ValueError: 3 is not in list

my_copy_list.sort()
print("List after sorting:", my_copy_list)

my_copy_list.reverse()
print("List after reversing :", my_copy_list)

print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])
