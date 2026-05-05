# Program to find the intersection and difference between two sets and values are taken from the user
#.....................................................................
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
# finding the intersection of the two sets
intersection = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection)
# finding the difference between the two sets
difference = set1.difference(set2)
print("Difference between set1 and set2:",difference)
