

# Library Management System

A **simple Python program** to manage a library with books and members. You can add books, register members, borrow and return books, check availability, and display library status.

The program also supports **reading commands from a file** (`commands.txt`) for easy testing.

---

## Features

* Add new books to the library.
* Register new members.
* Borrow and return books.
* Check availability of a book.
* Display all books borrowed by a member.
* Display the full library status with all books and members.
* Read commands from a file to execute multiple operations sequentially.

---

## Files

1. **library.py** – Main Python script containing all classes and logic.
2. **commands.txt** – Optional file containing commands to run the library system. Each command should be on a new line.

---

## Code Explanation

### 1. Classes

#### `Book`

Represents a book in the library.

* `id` – Unique book ID.
* `title` – Book title.
* `author` – Book author.
* `total` – Total copies of the book.
* `available` – Copies currently available.

#### `Member`

Represents a library member.

* `id` – Unique member ID.
* `name` – Member name.
* `borrowed_books` – List of borrowed book IDs.

#### `Library`

Main class that manages books and members.

* `books` – Dictionary of `Book` objects (`book_id: Book`).
* `members` – Dictionary of `Member` objects (`member_id: Member`).
* `nxt_book_id` – Next book ID to assign.
* `nxt_member_id` – Next member ID to assign.

---

### 2. Library Methods

| Method                            | Description                                                                       |
| --------------------------------- | --------------------------------------------------------------------------------- |
| `add_book(title, author, copies)` | Adds a book to the library with a unique ID.                                      |
| `register_member(name)`           | Registers a new member with a unique ID.                                          |
| `borrow_book(member_id, book_id)` | Allows a member to borrow a book if copies are available. Max 3 books per member. |
| `return_book(member_id, book_id)` | Returns a borrowed book back to the library.                                      |
| `check_availability(book_id)`     | Displays how many copies of a book are available.                                 |
| `display_member_books(member_id)` | Shows all books currently borrowed by a member.                                   |
| `display_library_status()`        | Shows the full status of the library including books and members.                 |

---

### 3. Main Program

The program can be run **with a command file**:

```bash
python3 library.py commands.txt
```

* `commands.txt` contains one command per line.
* Commands include:

```
add_book "Book Title" "Author Name" <number_of_copies>
register_member "Member Name"
borrow_book <member_id> <book_id>
return_book <member_id> <book_id>
check_availability <book_id>
display_member_books <member_id>
display_library_status
```

* Quotes `" "` are required if the title or author contains spaces.
* Example:

```
add_book "The Great Gatsby" "F. Scott Fitzgerald" 2
register_member "Alice Johnson"
borrow_book 1 1
check_availability 1
display_member_books 1
```

---

### 4. Important Notes

* Member IDs and Book IDs start at 1 and increment automatically.
* Each member can borrow **up to 3 books** at a time.
* If you try to borrow a book that doesn’t exist or has no available copies, the program will show an error message.
* `shlex.split()` is used to correctly handle spaces in book titles and author names.

---

### 5. Example Output

```
"The Great Gatsby" by F. Scott Fitzgerald added with book ID 1 (2 copies)
"Alice Johnson" is registered with member ID 1
"Alice Johnson" borrowed "The Great Gatsby" successfully.
Book ID 1 availability: 1 copies available
Books borrowed by Alice Johnson:
- The Great Gatsby by F. Scott Fitzgerald
------ Library Status ------
Books in the library:
- ID: 1, Title: The Great Gatsby, Author: F. Scott Fitzgerald, Available: 1/2
Library Members:
- ID: 1, Name: Alice Johnson, Borrowed: 1 books
```

---

### 6. How to Test

1. Save `library.py` in a folder.
2. Create a `commands.txt` with the commands you want to test.
3. Run:

```bash
python3 library.py commands.txt
```

4. Observe outputs for borrowing, returning, availability checks, and library status.


