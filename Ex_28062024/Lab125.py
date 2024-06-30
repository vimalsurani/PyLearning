class Password:

    def __init__(self, password):
        self.__password = password
        self.public_var = 10

    def get_password(self, is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("Invalid Password")

    def set_password(self, password):
        if password.endswith("9"):
            if len(password) > 10:
                self.__password = password
                print("Set Password is : ", self.__password)
            else:
                print("Not allowed, Weak Password")


pwd = Password("Abc123")
pwd.get_password(True)
pwd.set_password("123456789559")
