# library_management.py

class Book:
    """Represents a book in the library."""
    
    def __init__(self, title, author):
        self.title = title                  # Public attribute
        self.author = author                # Public attribute
        self._is_checked_out = False        # Private attribute: False = available

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available again)."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available, False if checked out."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of Book objects."""
    
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it exists and is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        # If not found or already checked out, do nothing (silent fail as per common design)

    def return_book(self, title):
        """Return a book by title if it exists."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return

    def list_available_books(self):
        """Print all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(str(book))