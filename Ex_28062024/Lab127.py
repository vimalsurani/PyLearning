class Addition:
    num1 = 0
    num2 = 0
    result = 0

    # parameterized constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def display(self):
        print("First number  = " + str(self.num1))
        print("Second number = " + str(self.num2))
        print("Addition of two numbers = " + str(self.result))

    def calculate(self):
        self.result = self.num1 + self.num2


# creating object of the class
# invoke parameterized constructor
obj1 = Addition(100, 200)

# creating second object of same class
obj2 = Addition(10, 20)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()
