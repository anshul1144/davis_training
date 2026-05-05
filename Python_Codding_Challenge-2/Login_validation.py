# Write a program to verify username and password.

# Function to validate login credentials
def validate_login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Login Failed"

# Get user input
username = input("Enter username: ")
password = input("Enter password: ")
result = validate_login(username, password)
print(result)

""" Output:
Enter username: admin
Enter password: 1234
Login Successful
"""