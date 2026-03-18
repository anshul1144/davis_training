# Program for shopkeeper to calculate total bill after discount without using funcrion.
#...................................................................
# Input the total bill amount
total_bill = float(input("Enter the total bill amount: "))

# Calculate the discount based on the total bill amount
if total_bill > 1000:
    discount = total_bill * 0.10  # 10% discount
    discount_percent = 10
elif total_bill > 500:
    discount = total_bill * 0.05  # 5% discount
    discount_percent = 5
else:
    discount = 0  # No discount
    discount_percent = 0
# Calculate the final bill amount after applying the discount
final_bill = total_bill - discount
# Print the discount percentage and final bill amount
print(f"You got {discount_percent}% discount.")
print(f"The final bill amount after discount is: {final_bill:.2f}")

#...................................................................

"""Output:
Enter the total bill amount: 1200
You got 10% discount.
The final bill amount after discount is: 1080.00
"""
