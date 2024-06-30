class BankAccount:

    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fun(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print("Your balance is ", self.balance)


hdfc_bank = BankAccount()
print(hdfc_bank.balance)
hdfc_bank.deposit(101)
hdfc_bank.show_balance()
hdfc_bank.deposit(99)
hdfc_bank.show_balance()
hdfc_bank.withdraw(199)
hdfc_bank.show_balance()










