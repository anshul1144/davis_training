# Program for shopkeeper to calculate total bill after discount.
# ....................................................................
# Input the total bill amount from the user
total_bill = float(input("Enter the total bill amount: "))
# Check the total bill amount and apply the appropriate discount
if total_bill > 1000:
    discount = total_bill * 0.10  # 10% discount
    discount_percentage = 10
elif total_bill > 500:
    discount = total_bill * 0.05  # 5% discount
    discount_percentage = 5
else:
    discount = 0  # No discount
    discount_percentage = 0
    
# Calculate the final bill amount after applying the discount
final_bill = total_bill - discount
# Print the discount percentage and the final bill amount
print(f"Discount Percentage: {discount_percentage}%")
print(f"Final Bill Amount after discount: {final_bill:.2f}")

"""Output:
Enter the total bill amount: 1200
Discount Percentage: 10%
Final Bill Amount after discount: 1080.00
"""

