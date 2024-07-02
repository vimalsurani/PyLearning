class GrandFather:
    def car(self):
        return "Old car"


class Father(GrandFather):
    def car(self):
        return "honda civic"


class Son(Father):
    def car(self):
        return "Lambo"


son = Son()
grandfather = GrandFather()
print(grandfather.car())
print(son.car())
