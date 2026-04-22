""" Custom Password Validator

Rules:
- Min 8 chars
- At least 1 uppercase, 1 lowercase, 1 digit

Use:
- string operations
- loops + conditionals
- Raise custom exception if invalid
"""


class InvalidPasswordError(Exception):
    """Raised when password does not satisfy rules."""


def validate_password(password):
    # Rule: minimum 8 characters
    if len(password) < 8:
        raise InvalidPasswordError("Password must be at least 8 characters.")

    has_upper = False
    has_lower = False
    has_digit = False

    # Check each character using loop
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    # Validate all conditions
    if not has_upper:
        raise InvalidPasswordError("Password must contain at least 1 uppercase letter.")
    if not has_lower:
        raise InvalidPasswordError("Password must contain at least 1 lowercase letter.")
    if not has_digit:
        raise InvalidPasswordError("Password must contain at least 1 digit.")

    return True


if __name__ == "__main__":
    pwd = input("Enter password: ")
    try:
        if validate_password(pwd):
            print("Password is valid.")
    except InvalidPasswordError as exc:
        print("Invalid password:", exc)
