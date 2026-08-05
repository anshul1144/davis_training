""" Design a simple Bank Account system. 
Create a class called BankAccount. 
 Data Members ● Account Number ● Account Holder Name ● Balance"""
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # deposit money into account if amount is positive
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return
        self.balance += amount
        print("Deposit successful.")
        print("Current Balance: ₹", self.balance)

    # withdraw money only when enough balance is available
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return
        if amount > self.balance:
            print("Not enough balance. Withdrawal failed.")
            return
        self.balance -= amount
        print("Withdrawal successful.")
        print("Current Balance: ₹", self.balance)

    # show current balance
    def check_balance(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder)
        print("Current Balance: ₹", self.balance)


# main program starts here
print("Welcome to the Bank Account program")
account_number = input("Enter Account Number: ")
account_holder = input("Enter Name: ")
opening_balance = float(input("Enter Opening Balance: "))

# create bank account object with given details
account = BankAccount(account_number, account_holder, opening_balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Choice: ")

    if choice == "1":
        amount = float(input("Enter Amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter Amount: "))
        account.withdraw(amount)
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        print("Thank you. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")