class Student:

    def __init__(self):
        self.name = input("Enter your name :")
        self.age = int(input("Enter your age :"))

    def displays(self):
        print(f"Name is : {self.name} ,Age is : {self.age}")


student = Student()
student.displays()
