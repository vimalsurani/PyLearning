# Develop a Python script that calculates the square and cube of a given number
# num = 2 sq - 4, c = 8

num = 2
sq = num ** 2
c = num ** 3

print(f"The square of {num} is: {sq}")
print(f"The cube of {num} is: {c}")

print(f"The square of 2 is: {2 ** 2}, The cube of 2 is: {2 ** 3}")

# Create a program that takes two numbers as input and prints whether
# the first number is greater than, less than, or equal to the second number

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num1 < num2:
#     print(f"{num1} is less than {num2}")
# else:
#     print(f"{num1} is equal to {num2}")

print(f"{num1} {'is greater than' if num1 > num2 else 'is less than' if num1 < num2 else 'is equal to'} {num2}")
