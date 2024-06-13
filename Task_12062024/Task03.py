# Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24

n = int(input("Enter a number: "))

# fact = 1     i =1   1*1  = 1
# fact = 1     i =2   1*2  = 2
# fact = 2     i =3   2*3  = 6
# fact = 6     i =4   6*4  = 24
# fact = 24    i =5   24*5 = 120

fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(f"Factorial of {n} is {fact}")
