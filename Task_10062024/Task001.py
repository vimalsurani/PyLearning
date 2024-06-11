# Explain the difference between the = operator and the == operator in Python.

# = -> Assignment Operator
# used to assign value to variable

x = 10  # x assigned to value 10
print(x)

# == -> Equality Operator -> it return always Boolean value
# used to compare two values

x = 50
y = 50
print(x == y)  # 50 = 50 Both values are same return - True

a = 50
b = 25
print(a == b)  # 50 = 25 Both values are different return - False

if a == b:
    print("a and b both values are same")  # R
else:
    print("a and b both values are different")

# What does the ** operator do in Python, and how is it used?

# ** - Exponentiation Operator (Power)
# used to raise one number to the power of another
# It supports both integer and floating-point numbers, as well as negative exponents

result1 = 2 ** 3  # 2 raised to the power of 3
print(result1)  # 2*2*2 =8

result2 = 5 ** 2  # 5 raised to the power of 2
print(result2)  # 5*5 = 25

# Negative Exponents

result3 = 2 ** -1
print(result3)  # 1/2 = 0.5

# Zero Exponent: Any number raised to the power of 0 is

result4 = 2 ** 0
print(result4)  # Always return 1

# What does the ^ operator do in Python, and in what context is it commonly used?

# ^ -> Bitwise XOR (exclusive OR) Operator
# binary operator that compares two binary digits and returns 1 if they are different, otherwise it returns 0
# a ^ b

result = 5 ^ 3  # 5 - 0101 ^ 3 - 0011
print(result)   # 6 - 0110


# Swapping Values without tem variable

a = 5
b = 9
a = a ^ b  # 5 ^ 9 = 12 (0101 ^ 1001 = 1100) -> a = 12 , b = 9
b = a ^ b  # 12 ^ 9 = 5 (1100 ^ 1001 = 0101) -> b = 5 , a = 12
a = a ^ b  # 12 ^ 5 = 9 (1100 ^ 0101 = 1001) -> a = 9 ,b = 5
print(a, b)







