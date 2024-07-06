num1 = int(input("Ent the num1"))  # ValueError: invalid literal for int() with base 10: 'ffw'
num2 = int(input("Ent the num2"))
result = num1 / num2  # ZeroDivisionError: division by zero

print("Result division is ", result)

# What are the different problem we can face?
# Why we want to handle this?

# ATM -> HDFC
# ATM -> HDFC -> Inserted card -> 5k
# Entered the amount, PIN, money got deducted, but you didn't get it
# via ATM, There is no message( not handled properly)


# Bad User Exp.
# User will curse you :)
# We need to handle it and give user a better exp.
