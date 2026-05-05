# Write a program to classify the user as Minor, Adult, or Senior.


# Function to classify age
def classify_age(age):
    if age < 18:
        return "Minor"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"
    
# Get user input
age = int(input("Enter your age: "))
category = classify_age(age)
print(f"You are classified as: {category}")

""" Output:
Enter your age: 25
You are classified as: Adult
"""