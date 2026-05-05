# Program to classify numbers as:
# 1) Positive / Negative / Zero
# 2) Even / Odd (using nested if)


def classify_number(number):
    if number > 0:
        sign = "Positive"
        if number % 2 == 0:
            parity = "Even"
        else:
            parity = "Odd"
    elif number < 0:
        sign = "Negative"
        if number % 2 == 0:
            parity = "Even"
        else:
            parity = "Odd"
    else:
        sign = "Zero"
        parity = "Even"

    return sign, parity


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

for num in numbers:
    sign, parity = classify_number(num)
    print(f"{num}: {sign}, {parity}")

""" Output: 
Enter numbers separated by spaces: 10 -5 0 7 -2
10: Positive, Even
-5: Negative, Odd
0: Zero, Even
7: Positive, Odd
"""