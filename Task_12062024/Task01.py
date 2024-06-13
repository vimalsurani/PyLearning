# Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# Input = 2024
# Output = Leap year

year = int(input("Enter Year:"))

# Divisible by 4   year % 4 == 0
# Not Divisible by 100  year % 100 != 0
# Divisible by 4  year % 400 == 0


# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

if year % 4 == 0:
    print(f"{year} is Leap Year")
else:
    print(f"{year} is Not a Leap Year")
