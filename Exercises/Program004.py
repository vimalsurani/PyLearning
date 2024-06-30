# Find Minimum of two numbers

# a = 15
# b = 4

# 1. Using min()

# print(min(a, b))

# # 2. Using loop

# if a < b:
#     print(f"{a} is minimum")
# else:
#     print(f"{b} is minimum")

# 3. Using function

# def minimum(a, b):
#     if a <= b:
#         return a
#     else:
#         return b
#
#
# print(minimum(a, b))

# 4. Using Ternary Operator

# print(a if a < b else b)


# 5. Using lambda

# minimum = lambda a, b: a if a < b else b
# print(f'{minimum(a,b)} is a minimum number')

# 6. Using sort() method

x, y, z = 12, 3, 4

xt = [x, y, z]
xt.sort()
print(xt[0])
