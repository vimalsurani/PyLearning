# Inverted pyramid pattern of numbers
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5


n = 5
count = 0

# outer loop
for i in range(n,0,-1):
    count = count+1

    # nested loop
    for j in range(1,i+1):
        # display number
        print(count, end=" ")
    # new line after each row
    print()
