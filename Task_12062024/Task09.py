# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria:
# Unit                   Price
# First 100 units        no charge
# Next 100 units         Rs 5 per unit
# After 200 units        Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)


unit = int(input("Enter a number of unit :"))

if unit <= 100:
    print("No Charge")
elif unit > 100 and unit<200:
    amt = (unit-100)*5
    print(f"Electricity bill amount is Rs. {amt} of {unit} unit")
else:
    amt=500+(unit-200)*10
    print(f"Electricity bill amount is  Rs. {amt} of {unit} unit")
