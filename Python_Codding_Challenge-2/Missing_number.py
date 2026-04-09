# Write a program to find missing number.

# Function to find the missing number in a sequence
def find_missing_number(sequence):
    n = len(sequence) + 1  # Total numbers in the complete sequence
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(sequence)  # Sum of the given sequence
    missing_number = total_sum - actual_sum  # The missing number is the difference
    return missing_number

# Get user input for the sequence
input_string = input("Enter a sequence of numbers (comma separated): ")
sequence = [int(num.strip()) for num in input_string.split(',')]
result = find_missing_number(sequence)
print(f"The missing number is: {result}")

""" Output:
Enter a sequence of numbers (comma separated): 1,2,4,5
The missing number is: 3
"""