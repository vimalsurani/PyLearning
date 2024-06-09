# strings
# In built functions
# Function - Repeat a task - usa a function
# print()
# input()
# type()
# format()
# max()
# min()
# sum()
# avg()

name = "Rahul"  # 0 to 4

print(name)
print(type(name))
print(id(name))  # id - memory address where is it stored 4789955
print(len(name))  # length of string - 1

name = name.upper()
print(name)
name = name.lower()
print(name)
a = name.count("R")
print(a)

print(name[0])
# print(name[5])  # IndexError: string index out of range

# Python - Immutable that can't be changed
name[0] = "A"  # str object does not support item assignment
 