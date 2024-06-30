# Find Maximum of two numbers

a = 15
b = 4

# 1. Using max()

# print(max(a, b))

# 2. Using loop

# if a > b:
#     print(f"{a} is maximum")
# else:
#     print(f"{b} is maximum")

# 3. Using function

# def maximum(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# print(maximum(a, b))

# 4. Using Ternary Operator

# print(a if a < b else b)


# 5. Using lambda

# maximum = lambda a, b: a if a > b else b
# print(f'{maximum(a,b)} is a maximum number')

# 6. Using sort() method

x = [a,b]
x.sort()
print(x[-1])
