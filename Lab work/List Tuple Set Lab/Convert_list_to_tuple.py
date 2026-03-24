# Convert a list into a tuple after removing duplicate elements.

# taking input from user for the list
numbers = []
n = int(input("Enter number of elements in the list: "))
for i in range(n):
    num = int(input("Enter element for the list: "))
    numbers.append(num)
# removing duplicate elements from the list
unique_numbers = list(set(numbers))
# converting the list to a tuple
numbers_tuple = tuple(unique_numbers)
# printing the tuple
print("Tuple with unique elements:", numbers_tuple)
#...............................................................................

""" Output:
Enter number of elements in the list: 7
Enter element for the list: 1
Enter element for the list: 2
Enter element for the list: 3
Enter element for the list: 2
Enter element for the list: 4
Enter element for the list: 1
Enter element for the list: 5
Tuple with unique elements: (1, 2, 3, 4, 5)
"""