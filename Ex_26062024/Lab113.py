class Calc:

    def __init__(self,a,b):
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


obj_refs = Calc(7,5)
result = obj_refs.sum()
print("Sum is ",result) 
result = obj_refs.sub()
print("Sub is ",result)
result = obj_refs.mul()
print("Mul is ",result)
result = obj_refs.div()
print("Div is ",result)
