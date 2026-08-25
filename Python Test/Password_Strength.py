"""Password strength checker and account login simulation."""

import string
import time


MAX_FAILED_ATTEMPTS = 3
LOCK_SECONDS = 10


def check_password(password):
	checks = {
		"length": len(password) >= 8,
		"uppercase": any(character.isupper() for character in password),
		"lowercase": any(character.islower() for character in password),
		"digit": any(character.isdigit() for character in password),
		"special character": any(character in string.punctuation for character in password),
	}
	score = sum(checks.values())
	levels = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
	suggestions = [
		f"Use at least 8 characters." if not checks["length"] else "",
		"Add an uppercase letter." if not checks["uppercase"] else "",
		"Add a lowercase letter." if not checks["lowercase"] else "",
		"Add a digit." if not checks["digit"] else "",
		"Add a special character." if not checks["special character"] else "",
	]
	return checks, levels[score], [suggestion for suggestion in suggestions if suggestion]


def display_password_report(password):
	checks, strength, suggestions = check_password(password)
	print("\nPassword checks:")
	for check, passed in checks.items():
		print(f"{check.title()}: {'Yes' if passed else 'No'}")
	print(f"Strength: {strength}")
	if suggestions:
		print("Suggestions:")
		for suggestion in suggestions:
			print(f"- {suggestion}")
	else:
		print("Your password meets all basic requirements.")


def login(saved_password):
	failed_attempts = 0
	locked_until = 0

	while True:
		if time.time() < locked_until:
			remaining = int(locked_until - time.time()) + 1
			print(f"Account is locked. Try again in {remaining} second(s).")
			return False

		password = input("Enter password to log in: ")
		if password == saved_password:
			print("Login successful.")
			return True

		failed_attempts += 1
		print(f"Incorrect password. Attempts left: {MAX_FAILED_ATTEMPTS - failed_attempts}")
		if failed_attempts >= MAX_FAILED_ATTEMPTS:
			locked_until = time.time() + LOCK_SECONDS
			print(f"Too many failures. Account locked for {LOCK_SECONDS} seconds.")
			return False


def password_security_program():
	print("Password Strength and Account Security")
	password = input("Create a password: ")
	display_password_report(password)

	print("\nLogin simulation")
	login(password)


if __name__ == "__main__":
	try:
		password_security_program()
	except EOFError:
		print("\nNo input received. Exiting the security program.")
