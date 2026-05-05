# Program for a shopkeeper wants to calculate total bill after discount. by using function.
# ....................................................................
# Function to calculate total bill after discount
def calculate_total_bill(original_price, discount_percentage):
    """
    Calculate total bill after applying discount based on the formula:
    Total Bill = Original Price - (Original Price * Discount Percentage / 100)
    """
    discount_amount = (original_price * discount_percentage) / 100
    total_bill = original_price - discount_amount
    return total_bill
# Input the original price and discount percentage from the user
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))
# Calculate the total bill after discount using the function
total_bill = calculate_total_bill(original_price, discount_percentage)
# Print the calculated total bill after discount
print(f"The total bill after applying a discount of {discount_percentage:.2f}% on ${original_price:.2f} is: ${total_bill:.2f}")
# ....................................................................

"""Output:
Enter the original price of the item: 100
Enter the discount percentage: 20
The total bill after applying a discount of 20.00% on $100.00 is: $80.00
"""