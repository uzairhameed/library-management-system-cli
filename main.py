
"""
Entry point for the Library Management System.
"""

from models.book import Book
from models.member import Member
from services.library import Library
from storage.json_storage import load_library, save_library
from exceptions import (BookNotFoundError,MemberNotFoundError,NoCopiesAvailableError,BookAlreadyBorrowedError, BookNotBorrowedError,)


def main():
    """Start the Library Management System."""

    # Load previously saved books and members.
    library = load_library()

    print("Welcome to the Library Management System!")

    # Keep displaying the menu until the user chooses Exit.
    while True:
        print("\n===== Library Management System =====")
        print("1. List all books")
        print("2. List all members")
        print("3. Add a book")
        print("4. Register a member")
        print("5. Search for a book")
        print("6. Issue a Book")
        print("7. Return a Book")
        print("8. Exit")

        # Read the user's menu choice.
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            # Retrieve and display every book.
            books = library.get_all_books()

            if not books:
                print("No books found.")
            else:
                for book in books:
                    print(
                        f"Title: {book.title} | "
                        f"Author: {book.author} | "
                        f"ISBN: {book.isbn} | "
                        f"Available copies: {book.copies_available}"
                    )

        elif choice == "2":
            # Retrieve and display every registered member.
            members = library.get_all_members()

            if not members:
                print("No members found.")
            else:
                for member in members:
                    print(
                        f"Name: {member.name} | "
                        f"Member ID: {member.member_id} | "
                        f"Borrowed books: {member.borrowed_books}"
                    )

        elif choice == "3":
            # Collect the book details from the user.
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")

            try:
                # Convert the number of copies from text to an integer.
                copies = int(input("Enter number of copies: "))

                # Create and add the book.
                book = Book(title, author, isbn, copies)
                library.add_book(book)

                # Save the updated library.
                save_library(library)
                print("Book added successfully!")

            except ValueError as error:
                # Handle invalid copy counts and validation errors.
                print(f"Invalid input: {error}")

        elif choice == "4":
            # Collect the member's details.
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")

            try:
                # Create and register the member.
                member = Member(name, member_id)
                library.register_member(member)

                # Save the updated library.
                save_library(library)
                print("Member registered successfully!")

            except ValueError as error:
                # Handle invalid member details or duplicate IDs.
                print(f"Invalid input: {error}")

        
        elif choice == "5":
            # Ask the user which book they want to find.
            isbn = input("Enter the ISBN of the book: ").strip()

            try:
                # Search for the book using the Library service.
                book = library.search_book(isbn)

                # Display the book's details.
                print("\nBook found!")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"ISBN: {book.isbn}")
                print(f"Available copies: {book.copies_available}")

            except BookNotFoundError as error:
                # Display a helpful message if the ISBN doesn't exist.
                print(f"Search failed: {error}")

        elif choice == "6":
            # Ask which book the member wants to borrow.
            isbn = input("Enter the ISBN of the book: ").strip()

            # Ask which member wants to borrow the book.
            member_id = input("Enter the member ID: ").strip()

            try:
                # Issue the book using the existing Library method.
                library.issue_book(isbn, member_id)

            except BookNotFoundError as error:
                # Handle cases where the requested book doesn't exist.
                print(f"Book error: {error}")

            except MemberNotFoundError as error:
                # Handle cases where the member isn't registered.
                print(f"Member error: {error}")

            except NoCopiesAvailableError as error:
                # Handle cases where every copy is already borrowed.
                print(f"Availability error: {error}")

            except BookAlreadyBorrowedError as error:
                # Prevent the same member from borrowing the same book twice.
                print(f"Borrowing error: {error}")

        elif choice == "7":
            # Ask which book the member wants to return.
            isbn = input("Enter the ISBN of the book: ").strip()

            # Ask which member is returning the book.
            member_id = input("Enter the member ID: ").strip()

            try:
                # Return the book using the existing Library method.
                library.return_book(isbn, member_id)

            except BookNotFoundError as error:
                # Handle a book that doesn't exist in the library.
                print(f"Book error: {error}")

            except MemberNotFoundError as error:
                # Handle a member who isn't registered.
                print(f"Member error: {error}")

            except BookNotBorrowedError as error:
                # Handle a book the member hasn't borrowed.
                print(f"Return error: {error}")

        elif choice == "8":
            # Save the latest data before exiting.
            save_library(library)
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices.
            print("Invalid choice. Please enter a number from 1 to 5.")


# Run the application only when this file is executed directly.
if __name__ == "__main__":
    main()
