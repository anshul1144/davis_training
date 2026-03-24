# Write a program to find all duplicate elements in a given list.

#............................................................
# taking input from user
numbers = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

# creating an empty list to store duplicate elements
duplicates = []

# iterating through the list to find duplicates
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

# printing the list of duplicate elements
print("Duplicate elements in the list:", duplicates)

#............................................................

""" Output Example:
Enter number of elements: 7
Enter element: 1
Enter element: 2
Enter element: 3
Enter element: 2
Enter element: 4
Enter element: 5
Enter element: 1
Duplicate elements in the list: [1, 2]
"""