
"""Tests for the Library Management System."""

import unittest

# Import the Book model and its custom validation exception.
from models.book import Book
from models.member import Member
from services.library import Library
from exceptions import (
    InvalidBookError, InvalidCopiesError,
    BookNotFoundError,
    MemberNotFoundError,
    NoCopiesAvailableError,
    BookAlreadyBorrowedError,
    BookNotBorrowedError,
)

class TestBook(unittest.TestCase):
    """Test the creation and validation of books."""

    def test_create_valid_book(self):
        """A book with valid details should be created successfully."""

        book = Book("Python Basics", "John Smith", "ISBN001", 5)

        self.assertEqual(book.title, "Python Basics")
        self.assertEqual(book.author, "John Smith")
        self.assertEqual(book.isbn, "ISBN001")
        self.assertEqual(book.copies_available, 5)

    def test_empty_title_raises_error(self):
        """An empty title should raise InvalidBookError."""

        with self.assertRaises(InvalidBookError):
            Book("", "John Smith", "ISBN001", 5)

    def test_negative_copies_raise_error(self):
        """Negative copies should raise InvalidCopiesError."""

        with self.assertRaises(InvalidCopiesError):
            Book("Python Basics", "John Smith", "ISBN001", -1)


class TestMember(unittest.TestCase):
    """Test the creation and validation of library members."""

    def test_create_valid_member(self):
        """A member with valid details should be created successfully."""

        member = Member("Uzair", "M001")

        self.assertEqual(member.name, "Uzair")
        self.assertEqual(member.member_id, "M001")
        self.assertEqual(member.borrowed_books, set())

    def test_empty_name_raises_error(self):
        """An empty member name should raise ValueError."""

        with self.assertRaises(ValueError):
            Member("", "M001")

    def test_empty_member_id_raises_error(self):
        """An empty member ID should raise ValueError."""

        with self.assertRaises(ValueError):
            Member("Uzair", "")


class TestLibrary(unittest.TestCase):
    """Test the Library service."""

    def setUp(self):
        """Create a fresh library before each test."""

        self.library = Library()
        self.book = Book("Python Basics", "John Smith", "ISBN001", 3)
        self.member = Member("Uzair", "M001")

    def test_add_book(self):
        """A book should be stored in the library."""

        self.library.add_book(self.book)

        # Search for the book using its ISBN.
        found_book = self.library.search_book("ISBN001")

        self.assertEqual(found_book.title, "Python Basics")
        self.assertEqual(found_book.copies_available, 3)

    def test_register_member(self):
        """A member should be registered successfully."""

        self.library.register_member(self.member)

        # Find the member using their ID.
        found_member = self.library.find_member("M001")

        self.assertEqual(found_member.name, "Uzair")
        self.assertEqual(found_member.member_id, "M001")

    def test_add_same_isbn_increases_copies(self):
        """Adding another book with the same ISBN should increase copies."""

        self.library.add_book(self.book)

        another_book = Book("Python Basics", "John Smith", "ISBN001", 2)
        self.library.add_book(another_book)

        found_book = self.library.search_book("ISBN001")

        self.assertEqual(found_book.copies_available, 5)

    def test_get_all_books(self):
        """The library should return all stored books."""

        self.library.add_book(self.book)

        books = self.library.get_all_books()

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].isbn, "ISBN001")

    def test_get_all_members(self):
        """The library should return all registered members."""

        self.library.register_member(self.member)

        members = self.library.get_all_members()

        self.assertEqual(len(members), 1)
        self.assertEqual(members[0].member_id, "M001")

    
    def test_issue_book(self):
        """Issuing a book decreases available copies by one."""

        self.library.add_book(self.book)
        self.library.register_member(self.member)

        self.library.issue_book("ISBN001", "M001")

        self.assertEqual(self.book.copies_available, 2)
        self.assertIn("ISBN001", self.member.borrowed_books)

    def test_return_book(self):
        """Returning a borrowed book restores one available copy."""

        self.library.add_book(self.book)
        self.library.register_member(self.member)

        self.library.issue_book("ISBN001", "M001")
        self.library.return_book("ISBN001", "M001")

        self.assertEqual(self.book.copies_available, 3)
        self.assertNotIn("ISBN001", self.member.borrowed_books)

    def test_cannot_issue_same_book_twice_to_member(self):
        """A member cannot borrow the same ISBN twice."""

        self.library.add_book(self.book)
        self.library.register_member(self.member)

        self.library.issue_book("ISBN001", "M001")

        with self.assertRaises(BookAlreadyBorrowedError):
            self.library.issue_book("ISBN001", "M001")

    def test_cannot_issue_book_when_no_copies_available(self):
        """Issuing a book with zero available copies should fail."""

        unavailable_book = Book(
            "Python Basics", "John Smith", "ISBN002", 0
        )
        self.library.add_book(unavailable_book)
        self.library.register_member(self.member)

        with self.assertRaises(NoCopiesAvailableError):
            self.library.issue_book("ISBN002", "M001")

    def test_cannot_return_book_not_borrowed(self):
        """A member cannot return a book they never borrowed."""

        self.library.add_book(self.book)
        self.library.register_member(self.member)

        with self.assertRaises(BookNotBorrowedError):
            self.library.return_book("ISBN001", "M001")

    def test_search_missing_book_raises_error(self):
        """Searching for a nonexistent book should fail."""

        with self.assertRaises(BookNotFoundError):
            self.library.search_book("UNKNOWN")

    def test_find_missing_member_raises_error(self):
        """Finding a nonexistent member should fail."""

        with self.assertRaises(MemberNotFoundError):
            self.library.find_member("UNKNOWN")
    


# Run the tests when this file is executed directly.
if __name__ == "__main__":
    unittest.main()
