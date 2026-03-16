# Program to find greatest digit in given number.
#..................................................
num = int(input("Enter a number: "))

# Display the input number
print("The input number is:", num)

# Initialize greatest digit to 0
greatest_digit = 0
# Loop through each digit in the number
while num > 0:
    # Get the last digit
    digit = num % 10
    # Update greatest digit if current digit is greater
    if digit > greatest_digit:
        greatest_digit = digit
    # Remove the last digit
    num = num // 10
# Display the greatest digit
print("The greatest digit is:", greatest_digit)

#.......................................................

""" Output:
Enter a number: 57329
The input number is: 57329
The greatest digit is: 9
"""