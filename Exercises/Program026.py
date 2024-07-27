# Write a program to accept two numbers from the user and calculate multiplication

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))


def mul(n1, n2):
    result = n1 * n2
    print(f"Multiplication of {num1} and {num2} is :", result)


mul(num1, num2)
