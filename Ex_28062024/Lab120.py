class Car:
    name = None

    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected123"   # _protected_var- allow to access withing module
        self.__private_var = "pass@123"        # private_var -within class allow to access private variables

    def __private_method(self):
        print("Protected!")

    def printName(self):
        self.__private_method()
        if self.__private_var == "123":
            print("Hi, 123")
        print("I am allowed to public variables")


# This is end of the class

i20 = Car()
i20.printName()
# alto.__private_var    # Outside class doesn't allow to access private variables
