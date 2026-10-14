
"""
Custom exceptions for the Library Management System.

Keeping exceptions in one file makes them reusable across
models, services, and the main application.
"""


class LibraryError(Exception):
    """Base exception for library-related errors."""
    pass


class InvalidBookError(LibraryError):
    """Raised when a book contains invalid information."""
    pass


class InvalidCopiesError(InvalidBookError):
    """Raised when the available copies value is invalid."""
    pass

class BookNotFoundError(LibraryError):
    """Raised when a requested book cannot be found."""
    pass


class NoCopiesAvailableError(LibraryError):
    """Raised when no copies of a book are available."""
    pass


class BookAlreadyBorrowedError(LibraryError):
    """Raised when a member already holds the requested book."""
    pass


class BookNotBorrowedError(LibraryError):
    """Raised when a member tries to return a book they haven't borrowed."""
    pass

class MemberNotFoundError(LibraryError):
    """Raised when a requested member does not exist."""
    pass