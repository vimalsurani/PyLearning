class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, balance):
        self.balance += balance

    def __withdraw(self, balance):
        self.balance -= balance

    def __show_balance(self):
        print("Your Balance is ", self.balance)

    def if_you_are_auth(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("Not Allowed")

    def if_you_are_auth_user(self, auth, balance):
        if auth:
            self.__withdraw(balance=balance)
        else:
            print("Not Allowed")


hdfc_bank = BankAccount()
hdfc_bank.deposit(200)
# hdfc_bank.if_you_are_auth(True)
# hdfc_bank.if_you_are_auth_user(True,50)
# hdfc_bank.if_you_are_auth(True)

secure_PIN = int(input("Enter you PIN to see Balance : "))
if secure_PIN == 123:
    hdfc_bank.if_you_are_auth(True)
else:
    hdfc_bank.if_you_are_auth(False)

secure_PIN = int(input("Enter you PIN to withdraw balance : "))
if secure_PIN == 123:
    hdfc_bank.if_you_are_auth_user(True, 50)
    hdfc_bank.if_you_are_auth(True)
else:
    hdfc_bank.if_you_are_auth_user(False, 50)
