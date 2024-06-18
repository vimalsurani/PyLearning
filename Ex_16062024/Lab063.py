def print_argument(*args):  # ["Vims","Raj","Milan"]
    for i in args:
        print(i, end="\n")


# *args -> List
a = ["vims", "raj", "milan"]
for i in a:
    print(i)

for i in range(1, 5):
    print(i)

print_argument("vims", "raj", "milan")
