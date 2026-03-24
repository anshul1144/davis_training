# Flatten a nested list.
#......................................................................
# taking input from user for the nested list
n = int(input("Enter number of sublists: "))
nested_list = []
for i in range(n):
    sublist_size = int(input("Enter number of elements in sublist {}: ".format(i + 1)))
    sublist = []
    for j in range(sublist_size):
        num = int(input("Enter element for sublist {}: ".format(i + 1)))
        sublist.append(num)
    nested_list.append(sublist)
# flattening the nested list
flattened_list = [item for sublist in nested_list for item in sublist]
# printing the flattened list
print("Flattened list:", flattened_list)

""" Output:
Enter number of sublists: 3
Enter number of elements in sublist 1: 3
Enter element for sublist 1: 1
Enter element for sublist 1: 2
Enter element for sublist 1: 3
Enter number of elements in sublist 2: 2
Enter element for sublist 2: 4
Enter element for sublist 2: 5
Enter number of elements in sublist 3: 4
Enter element for sublist 3: 6
Enter element for sublist 3: 7
Enter element for sublist 3: 8
Enter element for sublist 3: 9
Flattened list: [1, 2, 3, 4, 5,
6, 7, 8, 9]
"""