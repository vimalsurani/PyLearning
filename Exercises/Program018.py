# Inverted Pyramid pattern with the same digit Pattern: –
# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5

n = 5

# outer loop
for i in range(n, 0, -1):
    # nested loop
    for j in range(0, i):
        # display number
        print(n, end=" ")
    # new line after each row
    print()
