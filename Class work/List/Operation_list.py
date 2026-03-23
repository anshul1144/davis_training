# Program to create a list of array 15 numbers and ask the user to input any other no. search this element intothe list and remove all the occurance from the list including its first occurance.

# creating a list of 15 numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# asking the user to input a number
num = int(input("Enter a number to search and remove from the list: "))
# searching for the number in the list and removing all occurrences
while num in numbers:
    numbers.remove(num)
# printing the updated list
print("Updated list after removing all occurrences of", num, ":", numbers)

""" Output:
Enter a number to search and remove from the list: 5
Updated list after removing all occurrences of 5 : [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
"""