# A shopkeeper wants to calculate total bill after discount.

# ....................................................................
price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

final_price = price * (100 - discount) / 100

print(f"Final price after discount: {final_price}")
# ....................................................................
"""
Output:
Enter price: 200
Enter discount percentage: 20
Final price after discount: 160.0
"""