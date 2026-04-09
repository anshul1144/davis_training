# Write a program to calculate total weekly sales.


# Function to calculate total weekly sales
def calculate_weekly_sales(daily_sales):
    total_sales = sum(daily_sales)
    return total_sales
# Get user input for daily sales
daily_sales = []
for i in range(7):
    sale = float(input(f"Enter sales for day {i+1}: "))
    daily_sales.append(sale)
total_weekly_sales = calculate_weekly_sales(daily_sales)
print(f"Total weekly sales: {total_weekly_sales:.2f}")

""" Output:
Enter sales for day 1: 100
Enter sales for day 2: 200
Enter sales for day 3: 150
Enter sales for day 4: 300
Enter sales for day 5: 250
Enter sales for day 6: 400
Enter sales for day 7: 100
Total weekly sales: 1500.00
"""