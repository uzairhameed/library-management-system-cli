
"""
Contains the Library class and its core management operations.
"""

from models.book import Book
from models.member import Member
from exceptions import BookNotFoundError, MemberNotFoundError,BookAlreadyBorrowedError,BookNotBorrowedError,NoCopiesAvailableError


class Library:
    """Manages books and registered library members."""

    def __init__(self):
        # Dictionaries allow quick lookup using ISBN or member ID.
        self.books = {}
        self.members = {}

    def add_book(self, book):
        """Add a Book object to the library."""

        # Ensure the provided object is a Book.
        if not isinstance(book, Book):
            raise TypeError("Expected a Book object.")

        # Use ISBN as the unique key.
        # If the ISBN already exists, increase its available copies.
        if book.isbn in self.books:
            self.books[book.isbn].copies_available += book.copies_available
        else:
            self.books[book.isbn] = book

    def register_member(self, member):
        """Register a Member object."""

        # Ensure the provided object is a Member.
        if not isinstance(member, Member):
            raise TypeError("Expected a Member object.")

        # Member IDs must be unique.
        if member.member_id in self.members:
            raise ValueError("Member ID already exists.")

        self.members[member.member_id] = member

    def search_book(self, isbn):
        """Find and return a book using its ISBN."""

        # Return the matching book or raise a clear error.
        if isbn not in self.books:
            raise BookNotFoundError(f"No book found with ISBN: {isbn}")

        return self.books[isbn]

    def find_member(self, member_id):
        """Find and return a member using their ID."""

        if member_id not in self.members:
            raise MemberNotFoundError(
                f"No member found with ID: {member_id}"
            )

        return self.members[member_id]

    
    def issue_book(self, isbn, member_id):
        """Issue one copy of a book to a registered member."""

        # Step 1: Find the requested book.
        book = self.search_book(isbn)

        # Step 2: Find the member who wants to borrow it.
        member = self.find_member(member_id)

        # Step 3: Check whether the member already has this book.
        if isbn in member.borrowed_books:
            raise BookAlreadyBorrowedError(
                f"{member.name} has already borrowed this book."
            )

        # Step 4: Ensure at least one copy is available.
        if book.copies_available <= 0:
            raise NoCopiesAvailableError(
                f"No copies of '{book.title}' are available."
            )

        # Step 5: Update the library's records.
        book.copies_available -= 1
        member.borrowed_books.add(isbn)

        print(f"'{book.title}' issued successfully to {member.name}.")


    
    def return_book(self, isbn, member_id):
        """Return a previously borrowed book to the library."""

        # Step 1: Find the book and the member.
        book = self.search_book(isbn)
        member = self.find_member(member_id)

        # Step 2: Check whether this member borrowed the book.
        if isbn not in member.borrowed_books:
            raise BookNotBorrowedError(
                f"{member.name} has not borrowed '{book.title}'."
            )

        # Step 3: Update the library's records.
        member.borrowed_books.remove(isbn)
        book.copies_available += 1

        print(f"'{book.title}' returned successfully by {member.name}.")

    
    def get_all_books(self):
        """Return a list containing all books in the library."""

        # Convert the books dictionary values into a list.
        return list(self.books.values())

    def get_all_members(self):
        """Return a list containing all registered members."""

        # Convert the members dictionary values into a list.
        return list(self.members.values())



