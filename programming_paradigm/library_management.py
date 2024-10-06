# library_management.py

class Book:
    """A class to represent a book in the library."""
    
    def __init__(self, title, author):
        """Initialize the book with a title and author, and set it as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Check out the book."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class to represent a collection of books in the library."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.check_out():
                print(f"You have checked out '{title}'.")
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and book.return_book():
                print(f"You have returned '{title}'.")
                return
        print(f"'{title}' was not checked out.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books.")
