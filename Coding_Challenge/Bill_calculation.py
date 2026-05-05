# Program to calculate discount with validation
# ....................................................................
price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

if price > 0 and 0 <= discount <= 100:
    print(f"Final price after discount: {price - price*discount/100}")
else:
    print("Invalid input")
# ....................................................................
"""
Output:
Enter price: 100
Enter discount: 10
Final price after discount: 90.0
"""