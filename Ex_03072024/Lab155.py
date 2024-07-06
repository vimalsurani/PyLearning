class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


balance = 100
withdraw = int(input("Enter the amount!"))
if withdraw > balance:
    raise Exception("Balance is Low!!")
else:
    print("Remaining Balance is : ", (balance - withdraw))
