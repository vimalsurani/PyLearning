# Read line number 4 from the following file
# Create a test.txt file and add the below content to it.
# test.txt file:
# line1
# line2
# line3
# line4
# line5
# line6
# line7

try:
    with open("test.txt", "r") as fp:
        lines = fp.readlines()
        print(lines[0])
finally:
    fp.close()
