#Write a Python program to calculate the bonus amount using given rules.

def calculate_bonus(salary):
    if salary <= 10000:
        bonus = salary * 0.05
    elif salary <= 20000:
        bonus = salary * 0.10
    elif salary <= 30000:
        bonus = salary * 0.15
    elif salary <= 40000:
        bonus = salary * 0.20
    else:
        bonus = salary * 0.25
    return bonus

# Get user input
salary = float(input("Enter the salary amount: "))
bonus_amount = calculate_bonus(salary)
print(f"Bonus = {bonus_amount:.2f}")

""" Output: 
Enter the salary amount: 15000
Bonus = 1500.00
"""

