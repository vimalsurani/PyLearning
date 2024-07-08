# Write a program to find how many times substring “Emma” appears in the given string.

# str_x = "Emma is good developer. Emma is a writer"
#
# print(str_x.count("Emma"))


def check_substring(str_x):
    count = 0
    for i in range(len(str_x) - 1):
        count += str_x[i: i + 4] == 'Emma'
    return count


count = check_substring("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")

