""" Display last N lines of a file efficiently (like Linux tail)."""

from collections import deque


def tail(file_name="input.txt", n=10):
    # deque with maxlen keeps only the last n lines in memory
    with open(file_name, "r", encoding="utf-8") as file:
        last_lines = deque(file, maxlen=n)

    for line in last_lines:
        print(line.rstrip())


if __name__ == "__main__":
    line_count = int(input("Enter number of last lines to display: "))
    tail(n=line_count)
