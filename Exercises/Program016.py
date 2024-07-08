# print the following half-pyramid pattern of numbers
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


n = 5

# outer loop
for i in range(1, n + 1):
    # nested loop
    for j in range(1, i + 1):
        # display number
        print(j, end=" ")
    # new line after each row
    print()
