# Write a program to iterate the first 10 numbers, and in each iteration,
# print the sum of the current and previous number.

previous_num = 0

for i in range(11):
    current_number = i
    sum_num = i + previous_num
    print(f'Current Number {current_number} and Previous Number {previous_num} is sum : {sum_num}')
    previous_num = i
