income = float(input("Enter the annual income: "))

if income > 0:
    if income <= 85_528:
        tax = income * 0.18 - 556.02
    else: tax = 14_839.02 + 0.32 * (income - 85_528)
else: tax = 0

if tax < 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
