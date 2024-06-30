class LoginPage:
    def __init__(self, email, password, name):
        self.__email = email
        self.__password = password
        self.name = name
        self.__name = "abc"  #private

    def login_confirm(self):
        if self.__email == "vimal@gmail.com" and self.__password == "123":
            print("Allowed")
        else:
            print("Not Allowed")


loginpage = LoginPage("vimal@gmail.com", "123", "Vimal")
loginpage.login_confirm()
print(loginpage.name)
# print(loginpage.__email)
# loginpage.__email = "??"
# loginpage.__password = "??"
