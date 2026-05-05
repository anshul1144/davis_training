"""
Sales Data Aggregator

Input file format:
product,category,price,quantity

Tasks done:
1. Total sales per category
2. Highest selling product
3. Handle invalid rows using try-except
"""

import csv

# File path (you can change this path if needed)
file_name = "Class work/Quiz 1/sales_data.csv"

# Dictionary to store total sales by category
category_sales = {}

# Variables to track highest selling product
highest_product_name = None
highest_product_sales = 0.0

# Count invalid rows
invalid_row_count = 0


try:
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        # Skip header row
        header = next(reader, None)
        if header is None:
            print("File is empty.")

        # Read each data row (start=2 because header is line 1)
        for line_number, row in enumerate(reader, start=2):
            try:
                # Check row length first
                if len(row) != 4:
                    raise ValueError("Expected 4 values: product,category,price,quantity")

                product = row[0].strip()
                category = row[1].strip()
                price = float(row[2].strip())
                quantity = int(row[3].strip())

                # Check valid numeric values
                if price < 0 or quantity < 0:
                    raise ValueError("Price and quantity must be non-negative")

                # Calculate this row's sales
                sales_value = price * quantity

                # Add into category total
                if category in category_sales:
                    category_sales[category] += sales_value
                else:
                    category_sales[category] = sales_value

                # Track highest selling product (by sales value)
                if sales_value > highest_product_sales:
                    highest_product_sales = sales_value
                    highest_product_name = product

            except ValueError as error:
                invalid_row_count += 1
                print(f"Line {line_number}: Invalid row -> {error}")
            except Exception as error:
                invalid_row_count += 1
                print(f"Line {line_number}: Unexpected row error -> {error}")

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as error:
    print(f"Error while reading file: {error}")


# Final report
print("\n--- Sales Report ---")

print("\nTotal sales per category:")
if len(category_sales) == 0:
    print("No valid sales data found.")
else:
    for category, total in category_sales.items():
        print(f"{category}: {total:.2f}")

print("\nHighest selling product:")
if highest_product_name is None:
    print("No valid product found.")
else:
    print(f"{highest_product_name} (Sales: {highest_product_sales:.2f})")

print(f"\nInvalid rows skipped: {invalid_row_count}")
