def allowed_to_attend_class(name):
    match name:
        case "Dell":
            print("Dell is allowed")
        case "Vims":
            print("Vims is allowed")
        case "Raj":
            print("Raj is allowed")
        case _:
            print("not allowed")


allowed_to_attend_class("Vimal")
allowed_to_attend_class("Raj")
