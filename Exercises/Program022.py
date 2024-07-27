# Calculate income tax for the given income by adhering to the rules below
# Taxable Income	Rate (in %)
# First $10,000	    0
# Next $10,000	    10
# The remaining	    20

# Expected Output:
# For example, suppose the taxable income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000


income = int(input("Enter income : "))
tax_payable = 0
if income <= 10000:
    tax_payable = 0
    print(f"Taxable income is {income} and Total tax to pay is {tax_payable}")
elif income <= 20000:
    x = income - 10000
    tax_payable = x * 0.10
    print(f"Taxable income is {income} and Total tax to pay is {tax_payable}")
else:
    tax_payable = 0
    tax_payable = 10000 * 0.10
    tax_payable = tax_payable + (income - 20000) * 0.20
    print(f"Taxable income is {income} and Total tax to pay is {tax_payable}")
