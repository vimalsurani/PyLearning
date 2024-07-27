# Write a program to count the total number of digits in a number using a while loop.
#
num = 75869
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print("Total digits are:", count)