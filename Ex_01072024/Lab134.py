# Multiple Inheritance

class Father:

    def father_money(self):
        return 100

    def home(self):
        return "This is father house"


class Mother:

    def monther_money(self):
        return 150

    def home(self):
        return "This is mother house"


class Son(Father, Mother):
    pass

    # def home(self):
    #     return "This is son house"


# Problem - Diamond Problem - Java
# Python - Multiple Inheritance

son = Son()
print(son.father_money())
print(son.monther_money())
print(son.home())  # Method Resolution
