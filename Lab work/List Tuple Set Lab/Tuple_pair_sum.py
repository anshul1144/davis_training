# Program to find all pairs in a tuple whose sum equals a given value.
#......................................................................
# taking input from user for the tuple
n = int(input("Enter number of elements in the tuple: "))
tuple1 = ()
for i in range(n):
    num = int(input("Enter element for the tuple: "))
    tuple1 += (num,)
# taking input from user for the target sum
target_sum = int(input("Enter the target sum: "))
# finding pairs in the tuple whose sum equals the target sum
pairs = []
for i in range(len(tuple1)):
    for j in range(i + 1, len(tuple1)):
        if tuple1[i] + tuple1[j] == target_sum:
            pairs.append((tuple1[i], tuple1[j]))
# printing the pairs
if pairs:
    print("Pairs in the tuple whose sum equals", target_sum, "are:")
    for pair in pairs:
        print(pair)
else:
    print("No pairs found in the tuple whose sum equals", target_sum)

""" Output:
Enter number of elements in the tuple: 5
Enter element for the tuple: 1
Enter element for the tuple: 2
Enter element for the tuple: 3
Enter element for the tuple: 4
Enter element for the tuple: 5
Enter the target sum: 5 
Pairs in the tuple whose sum equals 5 are:
(1, 4)
(2, 3)
"""