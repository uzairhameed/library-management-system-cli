
"""Tests for JSON storage."""

import json
import os
import tempfile
import unittest

from models.book import Book
from models.member import Member
from services.library import Library
from storage.json_storage import save_library, load_library


class TestJSONStorage(unittest.TestCase):
    """Test saving and loading library data."""

    def setUp(self):
        """Create a fresh library for each test."""

        self.library = Library()
        self.library.add_book(
            Book("Python Basics", "John Smith", "ISBN001", 3)
        )
        self.library.register_member(Member("Uzair", "M001"))

    def test_save_and_load_books_and_members(self):
        """Saved books and members should be restored correctly."""

        # Create a temporary file for this test.
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "library.json")

            # Save the library, then load it into a new instance.
            save_library(self.library, file_path)
            loaded_library = load_library(file_path)

            # Verify that the book and member were restored.
            self.assertEqual(
                loaded_library.search_book("ISBN001").title,
                "Python Basics",
            )
            self.assertEqual(
                loaded_library.find_member("M001").name,
                "Uzair",
            )

    def test_load_missing_file_returns_empty_library(self):
        """A missing file should produce an empty library."""

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "missing.json")

            loaded_library = load_library(file_path)

            self.assertEqual(loaded_library.get_all_books(), [])
            self.assertEqual(loaded_library.get_all_members(), [])

    def test_borrowing_records_survive_save_and_load(self):
        """Borrowed ISBNs and available copies should be preserved."""

        self.library.issue_book("ISBN001", "M001")

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "library.json")

            save_library(self.library, file_path)
            loaded_library = load_library(file_path)

            loaded_book = loaded_library.search_book("ISBN001")
            loaded_member = loaded_library.find_member("M001")

            self.assertEqual(loaded_book.copies_available, 2)
            self.assertIn("ISBN001", loaded_member.borrowed_books)


if __name__ == "__main__":
    unittest.main()
