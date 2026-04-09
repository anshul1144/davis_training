# Write a program to check if a number satisfies this condition.


# Function to check divisibility
def check_divisibiltity(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Yes"
    else:
        return "No"

# Get user input
number = int(input("Enter a number: "))
result = check_divisibiltity(number)
print(result)

""" Output:
Enter a number: 15
Yes
"""