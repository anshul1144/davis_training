"""Bank Transaction Processor

File contains:
account,type(deposit/withdraw),amount

Tasks:
- Compute final balance
- Prevent overdraft (raise exception)
"""


class OverdraftError(Exception):
    """Raised when withdrawal exceeds account balance."""


def process_transactions(file_name="transactions.csv"):
    balances = {}

    with open(file_name, "r", encoding="utf-8") as file:
        # Skip header if present
        first_line = file.readline().strip()
        if "account" not in first_line.lower():
            file.seek(0)

        for line_no, line in enumerate(file, start=2):
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) != 3:
                continue

            account, tx_type, amount_text = parts
            amount = float(amount_text)

            if account not in balances:
                balances[account] = 0.0

            if tx_type == "deposit":
                balances[account] += amount
            elif tx_type == "withdraw":
                if balances[account] < amount:
                    raise OverdraftError(
                        f"Overdraft on line {line_no} for account {account}"
                    )
                balances[account] -= amount

    print("Final balances:")
    for account, balance in balances.items():
        print(f"{account}: {balance:.2f}")


if __name__ == "__main__":
    try:
        process_transactions()
    except OverdraftError as exc:
        print("Transaction error:", exc)
