class Calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b


print("Sum is ", Calc(7, 5).sum())
print("Sub is ", Calc(7, 5).sub())
print("Mul is ", Calc(7, 5).mul())
print("Div is ", Calc(7, 5).div())
