# Palindrome of String
#
# i/p = naman , nitin, level
# o/p = true
#
# i/p = vimal
# o/p = false

# name = "Vimal" [::-1]
# print(name)

def palindrome(name):
    if name == name[::-1]:
        print(f"{name} is Palindrome String")
    else:
        print(f"{name} is not Palindrome String")


palindrome("nitin")
