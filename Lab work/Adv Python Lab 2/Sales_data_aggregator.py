""" Sales Data Aggregator

Given file:
product,category,price,quantity

Tasks:
- Total sales per category
- Highest selling product
- Handle invalid rows
"""


def aggregate_sales(input_file="sales.csv"):
    category_totals = {}
    product_sales = {}

    with open(input_file, "r", encoding="utf-8") as file:
        # Skip header if present
        first_line = file.readline().strip()
        if "product" not in first_line.lower():
            file.seek(0)

        for line_no, line in enumerate(file, start=2):
            try:
                parts = [p.strip() for p in line.strip().split(",")]
                if len(parts) != 4:
                    raise ValueError("Invalid column count")

                product, category, price_text, qty_text = parts
                price = float(price_text)
                qty = int(qty_text)
                if price < 0 or qty < 0:
                    raise ValueError("Negative price/quantity")

                sale_value = price * qty
                category_totals[category] = category_totals.get(category, 0) + sale_value
                product_sales[product] = product_sales.get(product, 0) + sale_value

            except Exception as exc:
                print(f"Skipped invalid row {line_no}: {exc}")

    highest_product = None
    highest_value = -1
    for product, value in product_sales.items():
        if value > highest_value:
            highest_value = value
            highest_product = product

    print("Total sales per category:")
    for category, total in category_totals.items():
        print(f"{category}: {total:.2f}")

    if highest_product is not None:
        print(f"Highest selling product: {highest_product} ({highest_value:.2f})")


if __name__ == "__main__":
    aggregate_sales()
