# Program to calculate discount using subtraction
# ....................................................................
price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

amount = price * discount / 100
print(f"Final price after discount: {price - amount}")
# ....................................................................
"""
Output:
Enter price: 300
Enter discount: 10
Final price after discount: 270.0
"""