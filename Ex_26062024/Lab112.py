class Calc:

    def sum(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b

    def sub(self, a, b):
        return a - b

    def div(self, a, b):
        return a / b


obj_refs = Calc()
result = obj_refs.sum(7, 5)
print("Sum is ",result)
result = obj_refs.sub(7, 5)
print("Sub is ",result)
result = obj_refs.mul(7, 5)
print("Mul is ",result)
result = obj_refs.div(7, 5)
print("Div is ",result)
