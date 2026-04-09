# Write a program to determine ticket price.


# Function to determine ticket price based on day
def calculate_ticket_price(day):
    day = day.lower()
    if day in ["saturday", "sunday"]:
        return 200
    elif day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
        return 100
    else:
        return "Invalid day"
# Get user input
day = input("Enter the day of the week: ")
price = calculate_ticket_price(day)
print(f"The ticket price for {day} is: {price}")

""" Output:
Enter the day of the week: Sunday
The ticket price for Sunday is: 200
"""