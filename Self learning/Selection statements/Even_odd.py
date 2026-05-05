# Program to check if a number is Even or Odd by validating the user input
while True:
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is an Even number.")
        else:
            print(f"{num} is an Odd number.")
        break  # Exit the loop after successful input and processing
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        
