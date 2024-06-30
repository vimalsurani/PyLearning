class LoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.email == "vimal@gmail.com" and self.password == "Pass123":
            print("Allow to enter")
        else:
            print("Not Allowed")


email = input("Enter your email : \n")
password = input("Enter your password : ")
amit = LoginPage(email, password)
amit.login_confirm()

email = input("Enter your email : \n")
password = input("Enter your password : ")

vimal = LoginPage(email,password)
vimal.login_confirm()
