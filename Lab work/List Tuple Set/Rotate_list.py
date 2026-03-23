# Rotate a list to the right by k positions.
# taking input from user
numbers = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)
k = int(input("Enter number of positions to rotate: "))
# rotating the list to the right by k positions
k = k % n  # to handle cases where k is greater than n
rotated_list = numbers[-k:] + numbers[:-k]
# printing the rotated list
print("Rotated list:", rotated_list)

""" Output Example:
Enter number of elements: 5
Enter element: 1
Enter element: 2
Enter element: 3
Enter element: 4
Enter element: 5
Enter number of positions to rotate: 2
Rotated list: [4, 5, 1, 2, 3]
"""