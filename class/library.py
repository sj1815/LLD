class Book:
    def __init__(self, title: str, author: str, isbn: str):
        # Initialize fields: title, author, isbn, is_available (starts as True)
        self._title = title
        self._author = author
        self._isbn = isbn
        self._is_available = True

    def borrow_book(self) -> bool:
        # Mark book as unavailable if currently available
        # Return True if successful, False if already borrowed
        if self._is_available:
            self._is_available = False
            return True
        return False

    def return_book(self) -> None:
        # Mark book as available
        self._is_available = True

    def display_info(self) -> None:
        # Print: "Title by Author (ISBN: isbn) - Available" or "- Borrowed"
        status = "Available" if self._is_available else "Borrowed"
        print(f"{self._title} by {self._author} (ISBN: {self._isbn}) - {status}")


if __name__ == "__main__":
    book = Book("The Pragmatic Programmer", "David Thomas", "978-0135957059")
    book.display_info()

    success = book.borrow_book()
    print(f"Borrow successful: {str(success).lower()}")
    book.display_info()

    success = book.borrow_book()
    print(f"Borrow successful: {str(success).lower()}")

    book.return_book()
    book.display_info()