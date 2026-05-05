"""Voting System with Duplicate Check

Input:
List of votes

Tasks:
- Count votes
- Prevent duplicate voting using set
- Declare winner
"""


def run_voting(votes):
    vote_count = {}
    voted_users = set()  # Prevent duplicate voting

    for voter_id, candidate in votes:
        if voter_id in voted_users:
            print(f"Duplicate vote ignored from voter: {voter_id}")
            continue

        voted_users.add(voter_id)
        vote_count[candidate] = vote_count.get(candidate, 0) + 1

    # Declare winner
    winner = None
    max_votes = -1
    for candidate, count in vote_count.items():
        if count > max_votes:
            max_votes = count
            winner = candidate

    print("Vote counts:", vote_count)
    if winner is not None:
        print(f"Winner: {winner} ({max_votes} votes)")


if __name__ == "__main__":
    sample_votes = [
        ("V1", "Alice"),
        ("V2", "Bob"),
        ("V1", "Bob"),
        ("V3", "Alice"),
    ]
    run_voting(sample_votes)
