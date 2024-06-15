browser = str(input("Enter the browser name\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code executed")
    case "firefox":
        print("Firefox code executed")
    case "edge":
        print("Edge code executed")
    case _:
        print("No browser Found!")
