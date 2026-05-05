
""" Create a function:

Initial balance = 10000
Ask withdrawal amount
Conditions:
Insufficient balance
Invalid amount (<0)
Successful withdrawal
Use while loop until user exits"""


def atm_withdraw_system():
    # Set initial account balance
    balance = 10000

    # Run loop until user chooses to exit
    while True:
        print(f"\nCurrent Balance: {balance}")
        amount = float(input("Enter withdrawal amount: "))

        # Check for invalid amount
        if amount < 0:
            print("Invalid amount")
        # Check for insufficient balance
        elif amount > balance:
            print("Insufficient balance")
        # Process successful withdrawal
        else:
            balance -= amount
            print("Successful withdrawal")
            print(f"Remaining Balance: {balance}")

        # Ask user if they want to continue
        choice = input("Do you want to withdraw again? (yes/no): ").lower()
        if choice == "no":
            print("Thank you for using ATM")
            break


# Run the ATM withdrawal function
atm_withdraw_system()
