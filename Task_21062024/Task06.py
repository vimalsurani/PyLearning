# Left Triangle Star Pattern
#
# n = 5
#
#     *
#    **
#   ***
#  ****
# *****

n = 5


def left_triangle():
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        print("*" * i)


left_triangle()
