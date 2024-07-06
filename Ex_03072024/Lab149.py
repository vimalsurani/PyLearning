# try :
#     # Try this code , if error
# except:
#     # Execute me if try has some error

print(" -- Start of the Program -- ")
try:
    num1 = int(input("Enter the num1 :"))  # ValueError: invalid literal for int() with base 10: 'ffw'
    num2 = int(input("Enter the num2 :"))
    result = num1 / num2  # ZeroDivisionError: division by zero
    print("Result division is ", result)
except Exception as e:
    print(e)
    print("Please enter integer!")


print(" -- End of the Program -- ")