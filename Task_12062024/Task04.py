# Fibonacci series
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 2, 3, 5, 8, 13


n = int(input("Enter the number:"))

a = 0
b = 1

print(a)

count = 1

while count < n:
    print(b)
    c = a + b
    a = b
    b = c
    count = count + 1
print(b)
