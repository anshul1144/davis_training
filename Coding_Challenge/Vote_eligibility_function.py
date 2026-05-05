# Program to check whether a person is eligible to vote or not by using function.
# ....................................................................
# Function to check voting eligibility
def check_voting_eligibility(age):
    """
    Check if the person is eligible to vote based on the age.
    A person is eligible to vote if their age is 18 or above.
    """
    if age >= 18:
        return "You are eligible to vote."
    elif age < 0:
        return "Invalid age. Age cannot be negative."
    else:
        return "You are not eligible to vote."
# Input the age of the person from the user
age = int(input("Enter your age: "))
# Check voting eligibility using the function
eligibility_message = check_voting_eligibility(age)
# Print the eligibility message
print(eligibility_message)
# ....................................................................

"""Output:
Enter your age: 20
You are eligible to vote.
"""