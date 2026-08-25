"""Simple library book management system."""


FINE_PER_DAY = 10


def add_book(books):
	book_id = input("Book ID: ").strip()
	if book_id in books:
		print("Book ID already exists.")
		return

	books[book_id] = {
		"title": input("Book title: ").strip(),
		"author": input("Author: ").strip(),
		"available": True,
		"borrower": "",
		"borrow_count": 0,
	}
	print("Book added successfully.")


def search_books(books):
	search = input("Search by title or author: ").strip().lower()
	matches = [
		(book_id, book)
		for book_id, book in books.items()
		if search in book["title"].lower() or search in book["author"].lower()
	]

	if not matches:
		print("No matching books found.")
		return
	for book_id, book in matches:
		status = "Available" if book["available"] else f"Issued to {book['borrower']}"
		print(f"{book_id} - {book['title']} by {book['author']} | {status}")


def issue_book(books):
	book_id = input("Book ID to issue: ").strip()
	if book_id not in books:
		print("Book not found.")
	elif not books[book_id]["available"]:
		print(f"Book is already issued to {books[book_id]['borrower']}.")
	else:
		books[book_id]["available"] = False
		books[book_id]["borrower"] = input("Borrower name: ").strip()
		books[book_id]["borrow_count"] += 1
		print("Book issued successfully.")


def read_non_negative_number(message):
	while True:
		try:
			number = int(input(message))
			if number >= 0:
				return number
			print("Enter a value greater than or equal to 0.")
		except ValueError:
			print("Enter a valid whole number.")


def return_book(books):
	book_id = input("Book ID to return: ").strip()
	if book_id not in books:
		print("Book not found.")
		return
	if books[book_id]["available"]:
		print("This book is not currently issued.")
		return

	days_late = read_non_negative_number("Days late (enter 0 if on time): ")
	fine = days_late * FINE_PER_DAY
	books[book_id]["available"] = True
	books[book_id]["borrower"] = ""
	print(f"Book returned. Late fine: {fine}")


def display_issued_books(books):
	issued_books = [book for book in books.values() if not book["available"]]
	if not issued_books:
		print("No books are currently issued.")
		return
	for book in issued_books:
		print(f"{book['title']} by {book['author']} | Borrower: {book['borrower']}")


def display_most_borrowed(books):
	if not books:
		print("No books available.")
		return
	most_borrowed = max(books.values(), key=lambda book: book["borrow_count"])
	print(
		f"Most frequently borrowed: {most_borrowed['title']} "
		f"({most_borrowed['borrow_count']} time(s))"
	)


def library_management():
	books = {}

	while True:
		print("\n1. Add book  2. Search  3. Issue  4. Return")
		print("5. Issued books  6. Most borrowed  7. Exit")
		choice = input("Choose an option: ").strip()

		if choice == "1":
			add_book(books)
		elif choice == "2":
			search_books(books)
		elif choice == "3":
			issue_book(books)
		elif choice == "4":
			return_book(books)
		elif choice == "5":
			display_issued_books(books)
		elif choice == "6":
			display_most_borrowed(books)
		elif choice == "7":
			print("Exiting the library system.")
			break
		else:
			print("Invalid choice.")


library_management()
