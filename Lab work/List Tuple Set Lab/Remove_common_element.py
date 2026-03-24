# Remove elements from the first list that are present in the second list.
#...........................................................................
# taking input from user for the first list
list1 = []
n1 = int(input("Enter number of elements in the first list: "))
for i in range(n1):
    num = int(input("Enter element for the first list: "))
    list1.append(num)
# taking input from user for the second list
list2 = []
n2 = int(input("Enter number of elements in the second list: "))
for i in range(n2):
    num = int(input("Enter element for the second list: "))
    list2.append(num)
    
#Displaying the first and second list
print("First list:", list1)
print("Second list:", list2)

# removing elements from the first list that are present in the second list
updated_list = [num for num in list1 if num not in list2]
# printing the updated list
print("Updated list after removing common elements:", updated_list)

""" Output:
Enter number of elements in the first list: 5
Enter element for the first list: 1
Enter element for the first list: 2
Enter element for the first list: 3
Enter element for the first list: 4
Enter element for the first list: 5
Enter number of elements in the second list: 3
Enter element for the second list: 2
Enter element for the second list: 4
Enter element for the second list: 6
Updated list after removing common elements: [1, 3, 5]
"""