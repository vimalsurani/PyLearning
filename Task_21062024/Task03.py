# String Reverse

# 3-4 ways to do this in Python
#
#
# name = "Vimal"[::-1]
# print(name)
#

def str_rev1(str_name):
    return str_name[::-1]


res = str_rev1("Vimal")
print(res)


def str_rev2(str_name):
    str_rev = ""
    for i in str_name:
        str_rev = i + str_rev
    return str_rev


print(str_rev2("Vimal"))


def str_rev3(str_name):
    return ''.join(reversed(str_name))


print(str_rev3("vimal"))
