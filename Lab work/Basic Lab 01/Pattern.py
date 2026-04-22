
""" Write a program:

Print triangle pattern using for loop
If row number is even → print *
If odd → print #"""
# Set how many rows to print in the triangle
rows = 4

# Loop through each row number from 1 to rows
for row in range(1, rows + 1):
    # Choose symbol based on row number
    if row % 2 == 0:
        symbol = "*"
    else:
        symbol = "#"

    # Print symbol repeated according to row count
    print(" ".join([symbol] * row))
