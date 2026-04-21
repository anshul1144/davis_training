"""
Fraud Transaction Detector

Rules to flag suspicious transactions:
1. Amount > threshold
2. Same user does multiple transactions within short time

Used concepts:
- loops
- conditions
- dictionary for flagged transactions
"""

# Sample transaction list
# time is in HH:MM format
transactions = [
    {"txn_id": "T101", "user": "U1", "amount": 1200, "time": "10:05"},
    {"txn_id": "T102", "user": "U2", "amount": 250, "time": "10:07"},
    {"txn_id": "T103", "user": "U1", "amount": 300, "time": "10:10"},
    {"txn_id": "T104", "user": "U3", "amount": 2000, "time": "10:12"},
    {"txn_id": "T105", "user": "U1", "amount": 150, "time": "10:14"},
    {"txn_id": "T106", "user": "U2", "amount": 1800, "time": "10:40"},
]

# Rule values
amount_threshold = 1000
short_time_minutes = 10


# Convert HH:MM into total minutes
def to_minutes(time_text):
    hour, minute = time_text.split(":")
    return int(hour) * 60 + int(minute)


# Dictionary to store flagged transaction data
# key   -> transaction id
# value -> details and reason list
flagged_transactions = {}


# Track last transaction time of each user
# example: {"U1": 605, "U2": 607}
last_user_time = {}


# Loop through each transaction and check fraud rules
for tx in transactions:
    txn_id = tx["txn_id"]
    user = tx["user"]
    amount = tx["amount"]
    time_text = tx["time"]
    current_time = to_minutes(time_text)

    reasons = []

    # Rule 1: High amount
    if amount > amount_threshold:
        reasons.append(f"Amount {amount} is greater than threshold {amount_threshold}")

    # Rule 2: Same user in short time
    if user in last_user_time:
        time_gap = current_time - last_user_time[user]
        if time_gap <= short_time_minutes:
            reasons.append(
                f"Same user made transactions within {time_gap} minutes"
            )

    # If we found any reason, store in dictionary
    if len(reasons) > 0:
        flagged_transactions[txn_id] = {
            "user": user,
            "amount": amount,
            "time": time_text,
            "reasons": reasons,
        }

    # Update last seen time for this user
    last_user_time[user] = current_time


# Print all flagged transactions
print("\n--- Flagged Transactions ---")

if len(flagged_transactions) == 0:
    print("No suspicious transactions found.")
else:
    for txn_id, details in flagged_transactions.items():
        print(f"\nTransaction ID: {txn_id}")
        print(f"User: {details['user']}")
        print(f"Amount: {details['amount']}")
        print(f"Time: {details['time']}")
        print("Reasons:")
        for reason in details["reasons"]:
            print(f"- {reason}")
