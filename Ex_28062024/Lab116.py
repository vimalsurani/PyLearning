class Person:
    # Class Variables / Instance Variables
    name = "Vimal"
    age = None

    def walk(self):
        a = 10 # Local Variables
        print("I am Method")
        print("Hello",self.age)


vimal = Person()
vimal.walk()
