
""" Write a function:

Input: salary and years of experience
Logic:
10 years → 20% bonus
5–10 years → 10%
<5 → 5%
Use if-elif-else
Loop for multiple employees"""


def calculate_bonus(salary, years_of_experience):
    # Decide bonus percentage using if-elif-else
    if years_of_experience >= 10:
        bonus_percent = 20
    elif years_of_experience >= 5:
        bonus_percent = 10
    else:
        bonus_percent = 5

    # Calculate bonus amount and total salary
    bonus_amount = salary * bonus_percent / 100
    total_salary = salary + bonus_amount

    return bonus_percent, bonus_amount, total_salary


# Ask how many employees to process
employee_count = int(input("Enter number of employees: "))

# Loop through each employee
for i in range(1, employee_count + 1):
    print(f"\nEmployee {i}")

    # Take salary and years of experience as input
    salary = float(input("Enter salary: "))
    experience = float(input("Enter years of experience: "))

    # Get bonus details from function
    percent, bonus, final_salary = calculate_bonus(salary, experience)

    # Display result for current employee
    print(f"Bonus Percentage: {percent}%")
    print(f"Bonus Amount: {bonus}")
    print(f"Total Salary: {final_salary}")
