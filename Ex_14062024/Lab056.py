def allowed_to_attend_python_class(name, password):
    if name == "Vimal":
        if password == "Yes":
            print("You are allowed to enter")
        else:
            print("Not allowed")


allowed_to_attend_python_class("Vimal", "Yes")
