# Method Overriding - Same name in the parent and child
# child always override the parent functions
# super means call my parent function

class Father:
    def home(self):
        print("Father's 1BHK House")


class Son(Father):
    def home(self):
        super().home()
        print("Son have No House")


pramod = Son()
pramod.home()
