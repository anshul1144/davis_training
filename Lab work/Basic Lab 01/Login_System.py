"""Create a login function:

Username = "admin", Password = "1234"
Allow max 3 attempts using a while loop
Use if-else for validation
Print:
"Login Successful"
"Account Locked" after 3 failures"""


def login_system():
    # Correct login credentials
    correct_username = "admin"
    correct_password = "1234"

    # Track current attempt count
    attempts = 0
    max_attempts = 3

    # Keep asking for credentials until success or attempts are over
    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Validate entered credentials
        if username == correct_username and password == correct_password:
            print("Login Successful")
            return
        else:
            attempts += 1
            print("Invalid credentials")

    # This runs only if all 3 attempts fail
    print("Account Locked")


# Run the login function
login_system()
