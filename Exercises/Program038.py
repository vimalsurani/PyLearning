# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

s = 0
n = int(input("Enter Number : "))

for i in range(1,n+1):
    s = s+i
print("\n")
print("Sum is: ", s)
