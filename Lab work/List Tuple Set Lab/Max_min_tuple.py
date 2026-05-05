# Find the maximum and minimum elements in a tuple without using built-in functions.

# taking input from user for the tuple
elements = []
n = int(input("Enter number of elements in the tuple: "))
for i in range(n):
    elem = int(input("Enter element for the tuple: "))
    elements.append(elem)
# converting list to tuple
my_tuple = tuple(elements)
# finding maximum and minimum elements in the tuple
max_element = my_tuple[0]
min_element = my_tuple[0]
for elem in my_tuple:
    if elem > max_element:
        max_element = elem
    if elem < min_element:
        min_element = elem
# printing the maximum and minimum elements
print(".........................................................................")
print("Maximum element in the tuple:", max_element)
print("Minimum element in the tuple:", min_element)

#...............................................................................

""" Output:
Enter number of elements in the tuple: 5
Enter element for the tuple: 3
Enter element for the tuple: 1
Enter element for the tuple: 4
Enter element for the tuple: 2
Enter element for the tuple: 5
...........................................................................
Maximum element in the tuple: 5
Minimum element in the tuple: 1
"""