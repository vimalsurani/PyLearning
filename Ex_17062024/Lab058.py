# Functions - Block of Code - Which can executed or reused.
# 1 Define
# 2 Call

# Built Functions -Which are created by the Python Contributors

result = max(2, 5)
print(result)

# User Defined
# They can return something
# They can't return -> non-return
# They have parameters
# They don't parameters / arguments
print("No Return Type and No Parameter / Argument")


def say_hi():  # No Return Type and No Parameter / Argument
    print("Hello")


say_hi()
print(say_hi())

print("No Return Type and No Parameter / Argument")


def say_hello_arg(name):  # No Return Type and with Argument
    print("Hello", name)


say_hello_arg("Vimal")
say_hello_arg("Raj")

print("No Return Type and with Default Argument")


def say_hello_arg_default(name="Vimal"):  # No Return Type and with Default Argument
    # Write the Code
    print("HI", name)


say_hello_arg_default()
say_hello_arg_default("Rajiv")
say_hello_arg_default(name="Meet")

print('Argument + return Type')


def sum_arg_ret(a, b, c):  # Argument + return Type
    return a + b / c


# result = sum_arg_ret(5, 8)
result = sum_arg_ret(5, 4, -5)
# result = sum_arg_ret(a=78, b=75, c=3)
# result = sum_arg_ret(b=101,a=99,c=3)
print(result)


