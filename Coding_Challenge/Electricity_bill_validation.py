# Program to calculate electricity bill based on units consumed by validation.
#..............................................................................

# Function to calculate electricity bill based on units consumed
def calculate_electricity_bill(units_consumed):
    bill_ammount =0.0
    if units_consumed <= 100:
        bill_ammount = units_consumed *0.5
    elif units_consumed <=200:
        bill_ammount = (100 * 0.5) + ((units_consumed - 100) * 0.75)
    elif units_consumed <=300:
        bill_ammount = (100 * 0.5) + (100 * 0.75) + ((units_consumed - 200) * 1.20)
    else:
        bill_ammount = (100 * 0.5) + (100 * 0.75) + (100 * 1.20) + ((units_consumed - 300) * 1.50)
    return bill_ammount

# Input the number of units consumed from the user
while True:
    try:
        units_consumed = float(input("Enter the number of units consumed: "))
        if units_consumed < 0:
            print("Units consumed cannot be negative. Please enter a valid number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value for units consumed.")
    # Calculate the electricity bill using the function
bill_amount = calculate_electricity_bill(units_consumed)
# Print the calculated bill amount
print(f"The electricity bill amount for {units_consumed} units is: ${bill_amount:.2f}")
#..............................................................................

"""Output:
Enter the number of units consumed: -50
Units consumed cannot be negative. Please enter a valid number.
Enter the number of units consumed: abc
Invalid input. Please enter a numeric value for units consumed.
Enter the number of units consumed: 350
The electricity bill amount for 350.0 units is: $425.00
"""