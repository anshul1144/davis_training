"""Extract valid email addresses from data.txt into emails.txt."""

import re


def extract_emails(input_file="data.txt", output_file="emails.txt"):
    # Basic email pattern for common valid addresses
    pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")

    with open(input_file, "r", encoding="utf-8") as infile:
        text = infile.read()

    emails = pattern.findall(text)

    # Write one email per line
    with open(output_file, "w", encoding="utf-8") as outfile:
        for email in emails:
            outfile.write(email + "\n")


if __name__ == "__main__":
    extract_emails()
    print("Emails saved to emails.txt")
