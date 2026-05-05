# Program Find common elements present in three lists.
#......................................................................
# taking input from user for the first list
n1 = int(input("Enter number of elements in the first list: "))
list1 = []
for i in range(n1):
    num = int(input("Enter element for the first list: "))
    list1.append(num)
# taking input from user for the second list
n2 = int(input("Enter number of elements in the second list: "))
list2 = []
for i in range(n2):
    num = int(input("Enter element for the second list: "))
    list2.append(num)
# taking input from user for the third list
n3 = int(input("Enter number of elements in the third list: "))
list3 = []
for i in range(n3):
    num = int(input("Enter element for the third list: "))
    list3.append(num)
# finding common elements in the three lists
common_elements = set(list1) & set(list2) & set(list3)
# printing the common elements
if common_elements:
    print("Common elements present in the three lists are:", common_elements)
else:
    print("No common elements found in the three lists.")
    
#............................................................................
""" Output:
Enter number of elements in the first list: 5
Enter element for the first list: 1     
Enter element for the first list: 2
Enter element for the first list: 3
Enter element for the first list: 4
Enter element for the first list: 5
Enter number of elements in the second list: 5
Enter element for the second list: 3
Enter element for the second list: 4
Enter element for the second list: 5
Enter element for the second list: 6
Enter element for the second list: 7
Enter number of elements in the third list: 5
Enter element for the third list: 5
Enter element for the third list: 6
Enter element for the third list: 7
Enter element for the third list: 8
Enter element for the third list: 9
Common elements present in the three lists are: {5}
"""
