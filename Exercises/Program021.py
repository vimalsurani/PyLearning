# Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

# n = 7536
# q1 = n % 10
# r1 = n // 10
# q2 = r1 % 10
# r2 = r1 // 10
# q3 = r2 % 10
# r3 = r2 // 10
# q4 = r3 % 10
# r4 = r3 // 10
#
# print(q1, sep=" ")
# print(q2)
# print(q3)
# print(q4)
#
# print(r1)
# print(r2)
# print(r3)
# print(r4)


# n = 7536
# for num in range(n):
#     if n > 0:
#         r = n % 10
#         n = n // 10
#         print(r, end=" ")


n = 7536
while n > 0:
    r = n % 10
    n = n // 10
    print(r, end=" ")





