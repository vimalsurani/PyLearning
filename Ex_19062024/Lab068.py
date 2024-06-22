# Function Scope

def my_func():
    a = 10
    local_var = 25
    print("Hello")
    print(a)


# print(a)  # NameError: name 'a' is not defined

my_func()
