"""
Defines the Book class and validates book information.
"""

from exceptions import InvalidBookError, InvalidCopiesError
from validators import validate_book_details, validate_copies

class Book:
    """
    Represents a single book in the library.

    Each book has a title, author, ISBN, and the number
    of copies currently available.
    """

    def __init__(self, title, author, isbn, copies_available):

         # Validate input before storing it.
        validate_book_details(title, author, isbn)
        validate_copies(copies_available)
        
        # Store the book's title, author, and unique ISBN.
        self.title = title
        self.author = author
        self.isbn = isbn

        # Track how many copies of this book are available to borrow.
        self.copies_available = copies_available
