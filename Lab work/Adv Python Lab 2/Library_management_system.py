"""Library Management System (Basic)

Features:
- Issue/return books
- Track availability
- Store records in file
"""

import json


def load_records(file_name="library_records.json"):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_records(records, file_name="library_records.json"):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)


def main():
    books = load_records()

    while True:
        print("\n1.Issue 2.Return 3.View 4.Save & Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            book = input("Book name: ").strip()
            if book not in books:
                books[book] = {"available": True, "issued_to": ""}

            if books[book]["available"]:
                user = input("Issue to: ").strip()
                books[book]["available"] = False
                books[book]["issued_to"] = user
                print("Book issued.")
            else:
                print("Book is already issued.")

        elif choice == "2":
            book = input("Book name: ").strip()
            if book in books and not books[book]["available"]:
                books[book]["available"] = True
                books[book]["issued_to"] = ""
                print("Book returned.")
            else:
                print("Book is not issued or not found.")

        elif choice == "3":
            print("Library records:")
            for book, info in books.items():
                print(book, info)

        elif choice == "4":
            save_records(books)
            print("Records saved.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
