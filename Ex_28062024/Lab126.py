# Default Constructor
class Person:

    # default constructor
    def __init__(self):
        self.first_name = "Vimal"
        self.last_name = "Patel"

    # method to printing data member
    def print_func(self):
        print(f"First Name is : {self.first_name}", f"Last Name is : {self.last_name}", sep="\n")


# creating object of class
name = Person()
name.print_func()
