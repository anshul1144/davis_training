# Program to check whether one set is a subset of another.
#......................................................................
# creating two sets of numbers
set1 = set()
set2 = set()
# taking input from user for the first set
n1 = int(input("Enter number of elements in the first set: "))
for i in range(n1):
    num = int(input("Enter element for the first set: "))
    set1.add(num)
# taking input from user for the second set
n2 = int(input("Enter number of elements in the second set: "))
for i in range(n2):
    num = int(input("Enter element for the second set: "))
    set2.add(num)
# checking whether set1 is a subset of set2
if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")
# checking whether set2 is a subset of set1
if set2.issubset(set1):
    print("Set2 is a subset of Set1")
else:
    print("Set2 is not a subset of Set1")

""" Output:
Enter number of elements in the first set: 3
Enter element for the first set: 1
Enter element for the first set: 2
Enter element for the first set: 3
Enter number of elements in the second set: 5 
Enter element for the second set: 1
Enter element for the second set: 2
Enter element for the second set: 3
Enter element for the second set: 4
Enter element for the second set: 5
Set1 is a subset of Set2
Set2 is not a subset of Set1
"""