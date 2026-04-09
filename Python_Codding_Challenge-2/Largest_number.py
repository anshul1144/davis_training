# Write a program to find the largest among three numbers.


# Function to find the largest among three numbers
def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

largest = find_largest(num1, num2, num3)
print(f"The largest number is: {largest}")

""" Output:
Enter the first number: 10
Enter the second number: 25
Enter the third number: 15
The largest number is: 25
"""