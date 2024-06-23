# Right Triangle Star Pattern
#
# n = 5
#
# *
# **
# ***
# ****
# *****


def right_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)


right_triangle(5)
