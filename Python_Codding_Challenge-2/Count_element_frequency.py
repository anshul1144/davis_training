# Write a program to count frequency of elements using dictionary.

# Function to count frequency of elements in a list
def count_element_frequency(input_list):
    frequency_dict = {}
    for element in input_list:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    return frequency_dict

# Get user input
input_string = input("Enter a list of numbers (comma separated): ")
input_list = [int(num.strip()) for num in input_string.split(',')]
result = count_element_frequency(input_list)
print(f"Frequency of elements: {result}")


""" Output:
Enter a list of numbers (comma separated): 1,2,2,3
Frequency of elements: {1: 1, 2: 2, 3: 1}
"""