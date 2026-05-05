# Program to calculate discount using round
# ....................................................................
price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

print(f"Final price after discount: {round(price-price*discount/100,2)}")
# ....................................................................
"""
Output:
Enter price: 100
Enter discount: 15
Final price after discount: 85.0
"""