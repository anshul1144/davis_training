"""
Custom Password Validator

Rules:
1. Minimum 8 characters
2. At least 1 uppercase letter
3. At least 1 lowercase letter
4. At least 1 digit

Concepts used:
- string operations
- loops + conditionals
- custom exception
"""


# Custom exception class
class InvalidPasswordError(Exception):
    pass


# Function to validate password
def validate_password(password):
    # Rule 1: minimum length check
    if len(password) < 8:
        raise InvalidPasswordError("Password must be at least 8 characters long.")

    has_upper = False
    has_lower = False
    has_digit = False

    # Loop through each character and check type
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    # Rule 2, 3, 4 checks
    if not has_upper:
        raise InvalidPasswordError("Password must contain at least 1 uppercase letter.")

    if not has_lower:
        raise InvalidPasswordError("Password must contain at least 1 lowercase letter.")

    if not has_digit:
        raise InvalidPasswordError("Password must contain at least 1 digit.")

    return True


# Take password input from user
user_password = input("Enter a password: ")

# Validate using try-except
try:
    if validate_password(user_password):
        print("Valid password")
except InvalidPasswordError as error:
    print(f"Invalid password: {error}")
except Exception as error:
    print(f"Something went wrong: {error}")
