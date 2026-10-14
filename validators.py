
"""
Validation functions for book data.
"""

from exceptions import InvalidBookError, InvalidCopiesError


def validate_book_details(title, author, isbn):
    """Validate a book's title, author, and ISBN."""

    # Ensure each field is a non-empty string.
    for field_name, value in [
        ("Book title", title),
        ("Author name", author),
        ("ISBN", isbn),
    ]:
        if not isinstance(value, str) or not value.strip():
            raise InvalidBookError(f"{field_name} cannot be empty.")


def validate_copies(copies_available):
    """Ensure available copies are a non-negative integer."""

    # Reject booleans as well, because bool is a subclass of int in Python.
    if isinstance(copies_available, bool) or not isinstance(copies_available, int):
        raise InvalidCopiesError("Available copies must be an integer.")

    if copies_available < 0:
        raise InvalidCopiesError("Available copies cannot be negative.")


def validate_member_details(name, member_id):
    """Validate a member's name and member ID."""

    # Ensure the member's name is a non-empty string.
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Member name cannot be empty.")

    # Ensure the member ID is a non-empty string.
    if not isinstance(member_id, str) or not member_id.strip():
        raise ValueError("Member ID cannot be empty.")
