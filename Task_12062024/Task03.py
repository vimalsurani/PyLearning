# Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24

n = int(input("Enter a number: "))

if n < 0:
    print("Invalid")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(f"Factorial of {n} is {fact}")
