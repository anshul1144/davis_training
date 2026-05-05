# Program to remove all empty sets from a list of sets.
#......................................................................
# creating a list of sets
list_of_sets = []
# taking input from user for the number of sets
n = int(input("Enter number of sets: "))
# taking input from user for each set
for i in range(n):
    set_size = int(input("Enter number of elements in set {}: ".format(i + 1)))
    current_set = set()
    for j in range(set_size):
        num = int(input("Enter element for set {}: ".format(i + 1)))
        current_set.add(num)
    list_of_sets.append(current_set)
# removing empty sets from the list of sets
non_empty_sets = [s for s in list_of_sets if s]
# printing the non-empty sets
print("Non-empty sets in the list:")
for s in non_empty_sets:
    print(s)

""" Output:
Enter number of sets: 4
Enter number of elements in set 1: 3
Enter element for set 1: 1
Enter element for set 1: 2
Enter element for set 1: 3
Enter number of elements in set 2: 0
Enter number of elements in set 3: 2
Enter element for set 3: 4
Enter element for set 3: 5
Enter number of elements in set 4: 0
Non-empty sets in the list:
{1, 2, 3}
{4, 5}
"""