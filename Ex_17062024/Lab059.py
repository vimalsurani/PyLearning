def say_hello_arg_default(name="Vimal"):
    print("Hi", name)


say_hello_arg_default()
say_hello_arg_default(name="Raj")
say_hello_arg_default("Path")


def sample_arg(x=5, y=9):
    print(f"Sum {x} and {y} is :", x + y)


sample_arg()
