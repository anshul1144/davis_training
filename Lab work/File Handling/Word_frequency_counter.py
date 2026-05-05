""" Count frequency of each word from article.txt (ignore case and punctuation)."""

import re
from collections import Counter


def count_word_frequency(input_file="article.txt"):
    # Read the full text content
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read().lower()

    # Extract only words (letters, digits, underscore)
    words = re.findall(r"\b\w+\b", text)

    # Count each word frequency
    frequencies = Counter(words)
    return frequencies


def main():
    word_counts = count_word_frequency()

    # Print all word counts in sorted word order
    for word in sorted(word_counts):
        print(f"{word}: {word_counts[word]}")


if __name__ == "__main__":
    main()
