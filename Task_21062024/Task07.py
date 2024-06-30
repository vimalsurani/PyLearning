# Full Triangle Star Pattern
#
# n = 5
#
# 123*
#   ***
#  *****
# *******

n = 5


def triangle():
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")

        for k in range(1, 2 * i):
            print("*", end="")
        print()


triangle()
