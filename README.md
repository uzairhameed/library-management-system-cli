# Library Management System

A command-line Library Management System built with Python. It allows users to manage books and library members, issue and return books, search by ISBN, and persist library data using JSON.

## Features

- **Book Management:** Add books and track available copies.
- **Member Management:** Register members with unique member IDs.
- **Book Search:** Search for books using their ISBN.
- **Issue Books:** Issue available books to registered members.
- **Return Books:** Return borrowed books and update availability.
- **JSON Persistence:** Save books, members, and borrowing records between application runs.
- **Custom Exceptions:** Handle missing books, missing members, unavailable copies, duplicate borrowing, and invalid returns.
- **Automated Tests:** Verify core functionality and JSON storage.

## Project Structure

```text
library-management-system/
├── models/
│   ├── __init__.py
│   ├── book.py
│   └── member.py
├── services/
│   ├── __init__.py
│   └── library.py
├── storage/
│   ├── __init__.py
│   ├── json_storage.py
│   └── library.json
├── tests/
│   ├── __init__.py
│   ├── test_library.py
│   └── test_storage.py
├── exceptions.py
├── validators.py
├── main.py
├── .gitignore
└── README.md
```

## Requirements

- Python 3.11 or compatible Python 3 version
- Git (optional, for cloning the repository)

No third-party Python packages are required for the current implementation.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/uzairhameed/library-management-system-cli.git
cd library-management-system
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Git Bash (Windows):**

```bash
source .venv/Scripts/activate
```

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Run the application

```bash
python main.py
```

Follow the menu to list books and members, add books, register members, search for books, issue books, and return books.

## Running Tests

Run the complete automated test suite:

```bash
python -m unittest discover -s tests -v
```

The tests cover book and member validation, library operations, exception handling, and JSON persistence.

## Data Storage

The application stores library data in `storage/library.json`. Books, registered members, and their borrowing records are saved so that data can be restored when the application starts again.

Keep this file in place when you want to preserve your local library data.

## Concepts Demonstrated

- Object-oriented programming (OOP)
- Classes and objects
- Data validation
- Custom exceptions
- Separation of concerns
- Dictionaries and sets
- JSON serialization and deserialization
- File handling
- Unit testing with `unittest`

## Future Improvements

- Handle corrupted or malformed JSON files.
- Add borrowing limits and due dates.
- Introduce a database such as SQLite.
- Improve input validation and error reporting.
- Add a graphical or web interface.

## License

Choose a license before distributing or accepting contributions to this project.
