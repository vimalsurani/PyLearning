num1 = input("Enter any number")
l = len(num1)

if l != 3:
    print("Enter three digit number")
else:
    print("Middle digit is ", (int(num1) % 100 // 10))
