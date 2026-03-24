# Program to merge two lists and return a sorted list of unique elements
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
# merging the two lists and removing duplicates
merged_list = list(set(list1 + list2))
# sorting the merged list
merged_list.sort()
# printing the sorted list of unique elements
print("Merged and sorted list of unique elements:", merged_list)

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
Merged and sorted list of unique elements: [1, 2, 3, 4, 5, 6, 7]
"""