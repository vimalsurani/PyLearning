# Assignment Operators  - To assign values to variables

x = 5
print("Assignment Operators ", x)

# += Addition Assignment Operator

x += 3  # x = x+3 = 5+3= 8
print("Addition Assignment Operator ", x)

# -= Subtraction Assignment Operator

x -= 3  # x = x - 3  = 8 -3 = 5
print("Subtraction Assignment Operator ", x)

# *= Multiplication Assignment Operator

x *= 3  # x = x * 3 = 5*3 = 15
print("Multiplication Assignment Operator ", x)

# /= Division Assignment Operator

x /= 3  # x = x / 3 = 15/3 = 5.0
print("Division Assignment Operator ", x)

# %= Modulus Assignment Operator - Quest

x %= 3  # x = x % 3 = 5 % 3 = 2.0
print("Modulus Assignment Operator ", x)

# //= Floor Division Assignment Operator - Rem
x = 11
x //= 3  # x = x // 3 = 11//3 = 3
print("Floor Division Assignment Operator ", x)

# **=	Exponentiation Assignment Operator
x **= 3  # x = x ** 3 = 3 ** 3 = 3*3*3 = 27
print("Exponentiation Assignment Operator ", x)

# &=	Bitwise AND Assignment Operator

x &= 3  # x = x & 3 = 27 & 3 = 3    11011 & 11 = 00011
print("Bitwise AND Assignment Operator ", x)

# |=	Bitwise OR Assignment Operator
x = 5
x |= 3  # x = x | 3 =  5 | 3 = 7     101 | 11 = 111 7
print("Bitwise OR Assignment Operator ", x)

# ^=	Bitwise XOR Assignment Operator
x ^= 3  # x = x ^ 3  111  011 = 100 4
print("Bitwise XOR Assignment Operator ", x)

# >>=	Bitwise Right Shift Assignment Operator
x = 8
x >>= 2  # x = x >> 3  1000 >> 2 = 0010 = 2
print("Bitwise Right Shift Assignment Operator ", x)

# <<=	Bitwise Left Shift Assignment Operator
x = 5
x <<= 3  # x = x << 3  101 << 3 = 101000 = 40
print("Bitwise Left Shift Assignment Operator ", x)

# :=	Walrus Operator
print(x := 3)  # x = 3


def sum1(a, b):
    return a + b


result = (int(input("enter number")) + int(input("enter number")))
print(result)
