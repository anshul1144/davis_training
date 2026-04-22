"""8) Search and print all lines containing a user-provided keyword."""


def keyword_search(file_name="input.txt"):
    # Ask user for keyword to search
    keyword = input("Enter keyword to search: ").lower()

    # Read file and print matching lines
    with open(file_name, "r", encoding="utf-8") as file:
        matches = []
        for line in file:
            if keyword in line.lower():
                matches.append(line.rstrip())

    if matches:
        print("Matching lines:")
        for line in matches:
            print(line)
    else:
        print("No matching lines found.")


if __name__ == "__main__":
    keyword_search()
