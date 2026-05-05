# Write a program to check if a number is positive, negative, or zero.


# Function to check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    
# Get user input
number = int(input("Enter a number: "))
result = check_number(number)
print(result)

""" Output:
Enter a number: -5
Negative
"""