# Program to find elements that are in either of the sets but not in both
# ......................................................................

# taking input from user for set 1
n1 = int(input("Enter number of elements in Set 1: "))
set1 = set()
for i in range(n1):
    num = int(input("Enter element for Set 1: "))
    set1.add(num)

# taking input from user for set 2
n2 = int(input("Enter number of elements in Set 2: "))
set2 = set()
for i in range(n2):
    num = int(input("Enter element for Set 2: "))
    set2.add(num)

# finding elements in either of the sets but not in both
result_set = set1.symmetric_difference(set2)

# printing the result
print("Elements in either set but not in both:", result_set)

"""
Output:
Enter number of elements in Set 1: 4
Enter element for Set 1: 1
Enter element for Set 1: 2
Enter element for Set 1: 3
Enter element for Set 1: 4
Enter number of elements in Set 2: 4
Enter element for Set 2: 3
Enter element for Set 2: 4
Enter element for Set 2: 5
Enter element for Set 2: 6
Elements in either set but not in both: {1, 2, 5, 6}
"""