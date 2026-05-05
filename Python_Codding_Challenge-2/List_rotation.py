# Write a program to rotate list by one position.

# Function to rotate list by one position
def rotate_list(input_list):
    if not input_list:
        return input_list
    last_element = input_list[-1]
    rotated_list = [last_element] + input_list[:-1]
    return rotated_list

# Get user input
input_string = input("Enter a list of numbers (comma separated): ")
input_list = [int(num.strip()) for num in input_string.split(',')]
result = rotate_list(input_list)
print(f"Rotated list: {result}")


""" Output:
Enter a list of numbers (comma separated): 1,2,3
Rotated list: [3, 1, 2]
"""