# Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

n = 5

# outer loop
for i in range(n+1):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=" ")
    # new line after each row
    print()
