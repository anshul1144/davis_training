# Program to calculate electricity bill based on units consumed.
# ....................................................................
# Input the number of units consumed from the user
units_consumed = float(input("Enter the number of units consumed: "))
# Initialize the bill amount
bill_amount = 0.0
# Calculate the bill amount based on the units consumed
if units_consumed <= 100:
    bill_amount = units_consumed * 0.5
elif units_consumed <= 200:
    bill_amount = (100 * 0.5) + ((units_consumed - 100) * 0.75)
elif units_consumed <= 300:
    bill_amount = (100 * 0.5) + (100 * 0.75) + ((units_consumed - 200) * 1.20)
else:
    bill_amount = (100 * 0.5) + (100 * 0.75) + (100 * 1.20) + ((units_consumed - 300) * 1.50)
# Print the calculated bill amount
print(f"The electricity bill amount for {units_consumed} units is: ${bill_amount:.2f}")

#.....................................................................

"""Output:
Enter the number of units consumed: 350
The electricity bill amount for 350.0 units is: $425.00
"""