""" Palindrome Sentence Analyzer

Given sentences:
- Detect palindrome words
- Count frequency
- Ignore spaces and case
"""

import re


def is_palindrome(word):
    clean = word.lower().replace(" ", "")
    return clean == clean[::-1]


def analyze_sentences(sentences):
    frequency = {}

    for sentence in sentences:
        words = re.findall(r"[A-Za-z0-9]+", sentence.lower())
        for word in words:
            if is_palindrome(word) and len(word) > 1:
                frequency[word] = frequency.get(word, 0) + 1

    print("Palindrome word frequency:")
    for word, count in frequency.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    sample = [
        "Madam and level are in this line",
        "Wow, radar sees civic duty",
    ]
    analyze_sentences(sample)
