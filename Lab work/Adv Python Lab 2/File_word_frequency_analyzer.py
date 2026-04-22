""" File Word Frequency Analyzer

Read a large file:
- Count word frequency
- Ignore stop words
- Show top 10 words
"""

import re
from collections import Counter


def analyze_words(file_name="large_text.txt"):
    stop_words = {
        "a", "an", "the", "is", "in", "on", "and", "or", "to", "of", "for", "with", "at", "by", "from", "as", "it"
    }

    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read().lower()

    words = re.findall(r"\b[a-z0-9']+\b", text)
    filtered = [w for w in words if w not in stop_words]

    counts = Counter(filtered)
    print("Top 10 words:")
    for word, freq in counts.most_common(10):
        print(f"{word}: {freq}")


if __name__ == "__main__":
    analyze_words()
