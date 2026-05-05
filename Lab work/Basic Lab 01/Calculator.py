
""" Create a function-based calculator:

Menu:
Add
Subtract
Multiply
Divide
Exit
Use while loop for repetition Use if-elif-else for operation selection Handle divide-by-zero using condition"""


def add(a, b):
    # Return addition result
    return a + b


def subtract(a, b):
    # Return subtraction result
    return a - b


def multiply(a, b):
    # Return multiplication result
    return a * b


def divide(a, b):
    # Handle divide-by-zero using condition
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def calculator():
    # Run calculator menu repeatedly until user exits
    while True:
        print("\nCalculator Menu")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Exit option check
        if choice == "5":
            print("Exiting calculator...")
            break

        # Validate operation choice using if-elif-else flow
        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(num1, num2))
            elif choice == "2":
                print("Result:", subtract(num1, num2))
            elif choice == "3":
                print("Result:", multiply(num1, num2))
            elif choice == "4":
                print("Result:", divide(num1, num2))
        else:
            print("Invalid choice, please select from 1 to 5")


# Start calculator program
calculator()
