# Program to Calculate electricity bill based on units consumed by using function.
# ....................................................................
# Function to calculate electricity bill based on units consumed
def calculate_electricity_bill(units_consumed):
    """
    Calculate the electricity bill amount based on the number of units consumed.
    The billing rates are as follows:
    - For the first 100 units: $0.50 per unit
    - For the next 100 units (101-200): $0.75 per unit
    - For the next 100 units (201-300): $1.20 per unit
    - For units above 300: $1.50 per unit
    """
    bill_amount = 0.0
    if units_consumed <= 100:
        bill_amount = units_consumed * 0.5
    elif units_consumed <= 200:
        bill_amount = (100 * 0.5) + ((units_consumed - 100) * 0.75)
    elif units_consumed <= 300:
        bill_amount = (100 * 0.5) + (100 * 0.75) + ((units_consumed - 200) * 1.20)
    else:
        bill_amount = (100 * 0.5) + (100 * 0.75) + (100 * 1.20) + ((units_consumed - 300) * 1.50)
    return bill_amount
# Input the number of units consumed from the user
units_consumed = float(input("Enter the number of units consumed: "))
# Calculate the electricity bill using the function
bill_amount = calculate_electricity_bill(units_consumed)
# Print the calculated bill amount
print(f"The electricity bill amount for {units_consumed} units is: ${bill_amount:.2f}")
#.....................................................................

"""Output:
Enter the number of units consumed: 350
The electricity bill amount for 350.0 units is: $425.00
"""