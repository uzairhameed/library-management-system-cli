"""
Functions for saving and loading library data using JSON.
"""

import json
from models.book import Book
from models.member import Member
from services.library import Library


def book_to_dict(book):
    """Convert a Book object into a dictionary for JSON storage."""

    # Convert the Book object's attributes into a dictionary.
    book_data = {
        "title": book.title,
        "author": book.author,
        "isbn": book.isbn,
        "copies_available": book.copies_available,
    }

    return book_data


def member_to_dict(member):
    """Convert a Member object into a dictionary for JSON storage."""

    # Convert the member's attributes into a dictionary.
    member_data = {
        "name": member.name,
        "member_id": member.member_id,

        # Convert the set into a list because JSON doesn't support sets.
        "borrowed_books": list(member.borrowed_books),
    }

    return member_data


def save_library(library, file_path="storage/library.json"):
    """Save all books and members from a Library object to a JSON file."""

    # Convert each Book object into a dictionary.
    books_data = [
        book_to_dict(book)
        for book in library.get_all_books()
    ]

    # Convert each Member object into a dictionary.
    members_data = [
        member_to_dict(member)
        for member in library.get_all_members()
    ]

    # Combine books and members into one dictionary.
    library_data = {
        "books": books_data,
        "members": members_data,
    }

    # Open the JSON file in write mode.
    # UTF-8 supports a wide range of characters.
    # The "with" statement automatically closes the file afterward.
    with open(file_path, "w", encoding="utf-8") as file:
        # Write the dictionary as readable JSON.
        json.dump(library_data, file, indent=4)

    print("Library data saved successfully.")


def book_from_dict(book_data):
    """Convert a dictionary into a Book object."""

    # Read the saved values and create a new Book object.
    book = Book(
        title=book_data["title"],
        author=book_data["author"],
        isbn=book_data["isbn"],
        copies_available=book_data["copies_available"],
    )

    return book


def member_from_dict(member_data):
    """Convert a dictionary into a Member object."""

    # Re-create the member using the saved name and ID.
    member = Member(
        name=member_data["name"],
        member_id=member_data["member_id"],
    )

    # Convert the saved list of ISBNs back into a set.
    member.borrowed_books = set(member_data["borrowed_books"])

    return member



def load_library(file_path="storage/library.json"):
    """Load library data from JSON, or return an empty library if missing."""

    # Create an empty library first.
    library = Library()

    try:
        # Open the JSON file in read mode.
        with open(file_path, "r", encoding="utf-8") as file:
            # Convert JSON data into a Python dictionary.
            library_data = json.load(file)

    except FileNotFoundError:
        # If no saved file exists, start with an empty library.
        return library

    # Restore all books from the saved data.
    for book_data in library_data["books"]:
        book = book_from_dict(book_data)
        library.add_book(book)

    # Restore all members from the saved data.
    for member_data in library_data["members"]:
        member = member_from_dict(member_data)
        library.register_member(member)

    return library
