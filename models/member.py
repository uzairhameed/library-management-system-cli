
from validators import validate_member_details

"""
Defines the Member class for the Library Management System.
"""


class Member:
    """Represents a registered library member."""

    def __init__(self, name, member_id):
         # Validate the member's details before storing them.
        validate_member_details(name, member_id)
       

        # Store the member's details without surrounding whitespace.
        self.name = name.strip()
        self.member_id = member_id.strip()

        # Store the ISBNs of books this member has borrowed.
        # A set prevents the same ISBN from being added twice.
        self.borrowed_books = set()
