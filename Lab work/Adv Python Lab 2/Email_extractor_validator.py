""" Email Extractor and Validator

From a text file:
- Extract emails
- Validate format
- Store unique emails
"""

import re


def extract_and_validate_emails(input_file="text_data.txt", output_file="valid_emails.txt"):
    pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")

    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    unique_emails = set(pattern.findall(text))

    with open(output_file, "w", encoding="utf-8") as out:
        for email in sorted(unique_emails):
            out.write(email + "\n")

    print(f"Saved {len(unique_emails)} unique valid emails.")


if __name__ == "__main__":
    extract_and_validate_emails()
