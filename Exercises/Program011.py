# Write a program to remove characters from a string
# starting from zero up to n and return a new string.

# For example:

# remove_chars("pynative", 4) so output must be tive.
# Here, we need to remove the first four characters from a string.

# remove_chars("pynative", 2) so output must be native.
# Here, we need to remove the first two characters from a string.


def remove_chars(str_name, n):         # with argument and return
    print('Original string:', str_name)
    new_str = str_name[n:]
    return new_str


print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
