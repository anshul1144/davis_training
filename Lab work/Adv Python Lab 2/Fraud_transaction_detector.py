"""Fraud Transaction Detector

Given a list of transactions:

Detect suspicious ones based on:
- Amount > threshold
- Same user multiple transactions within short time

Use:
- loops + conditions
- Store flagged data in dictionary
"""


def detect_fraud(transactions, amount_threshold=10000, time_gap_minutes=2):
    # Store flagged data in dictionary
    flagged = {"high_amount": [], "rapid_repeat": []}
    last_tx_time = {}

    for tx in transactions:
        user = tx["user"]
        amount = tx["amount"]
        tx_time = tx["time"]  # integer minute timestamp for simplicity

        # Condition 1: Amount above threshold
        if amount > amount_threshold:
            flagged["high_amount"].append(tx)

        # Condition 2: Same user multiple transactions within short time
        if user in last_tx_time and (tx_time - last_tx_time[user]) <= time_gap_minutes:
            flagged["rapid_repeat"].append(tx)

        last_tx_time[user] = tx_time

    return flagged


if __name__ == "__main__":
    sample_transactions = [
        {"user": "U1", "amount": 5000, "time": 10},
        {"user": "U1", "amount": 7000, "time": 11},
        {"user": "U2", "amount": 12000, "time": 15},
        {"user": "U3", "amount": 3000, "time": 20},
    ]

    result = detect_fraud(sample_transactions)
    print("Flagged Transactions:", result)
