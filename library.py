# Step 1: Define classes for Book and Member
class Book:
    def __init__(self, id, title, author, copies):
        self.id = id
        self.title = title
        self.author = author
        self.total = copies
        self.available = copies


class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []


# Step 2: Define the main Library class
class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.nxt_book_id = 1
        self.nxt_member_id = 1

    def add_book(self, title, author, copies):
        book = Book(self.nxt_book_id, title, author, copies)
        self.books[self.nxt_book_id] = book
        print(f'"{title}" by {author} added with book ID {self.nxt_book_id} ({copies} copies)')
        self.nxt_book_id += 1

    def register_member(self, name):
        member = Member(self.nxt_member_id, name)
        self.members[self.nxt_member_id] = member
        print(f'"{name}" is registered with member ID {self.nxt_member_id}')
        self.nxt_member_id += 1

    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print(f"Member ID {member_id} does not exist.")
            return
        if book_id not in self.books:
            print(f"Book ID {book_id} does not exist.")
            return
        member = self.members[member_id]
        book = self.books[book_id]
        if book.available <= 0:
            print(f'No copies of "{book.title}" are available.')
            return
        if len(member.borrowed_books) >= 3:
            print(f'"{member.name}" cannot borrow more than 3 books.')
            return
        member.borrowed_books.append(book_id)
        book.available -= 1
        print(f'"{member.name}" borrowed "{book.title}" successfully.')

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print(f"Member ID {member_id} does not exist.")
            return
        if book_id not in self.books:
            print(f"Book ID {book_id} does not exist.")
            return
        member = self.members[member_id]
        book = self.books[book_id]
        if book_id not in member.borrowed_books:
            print(f'"{member.name}" has not borrowed "{book.title}".')
            return
        member.borrowed_books.remove(book_id)
        book.available += 1
        print(f'"{member.name}" returned "{book.title}" successfully.')

    def check_availability(self, book_id):
        if book_id not in self.books:
            print(f"Book ID {book_id} not found")
            return
        book = self.books[book_id]
        word = "copy" if book.available == 1 else "copies"
        print(f'Book ID {book_id} availability: {book.available} {word} available')

    def display_member_books(self, member_id):
        if member_id not in self.members:
            print(f"Member ID {member_id} not found")
            return
        member = self.members[member_id]
        if not member.borrowed_books:
            print(f"Member {member.name} has not borrowed any books")
            return
        print(f"Books borrowed by {member.name}:")
        for book_id in member.borrowed_books:
            if book_id not in self.books:
                print(f"- Book ID {book_id} (not in library)")
                continue
            book = self.books[book_id]
            print(f"- {book.title} by {book.author}")

    def display_library_status(self):
        print("------ Library Status ------")
        if not self.books:
            print("No books in the library")
        else:
            print("Books in the library:")
            for book_id, book in self.books.items():
                print(f"- ID: {book.id}, Title: {book.title}, Author: {book.author}, Available: {book.available}/{book.total}")
        if not self.members:
            print("\nNo members in the library")
        else:
            print("\nLibrary Members:")
            for member_id, member in self.members.items():
                print(f"- ID: {member.id}, Name: {member.name}, Borrowed: {len(member.borrowed_books)} books")


# Step 3: Main entry point reading commands from a file
import sys
import shlex  # <- this handles quoted strings

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python library.py commands.txt")
        sys.exit(1)

    lib = Library()
    file = sys.argv[1]

    with open(file) as f:
        for line in f:
            parts = shlex.split(line)  # <-- fix to handle spaces in quotes
            if not parts:
                continue

            cmd = parts[0]

            if cmd == "add_book":
                lib.add_book(parts[1], parts[2], int(parts[3]))
            elif cmd == "register_member":
                lib.register_member(parts[1])
            elif cmd == "borrow_book":
                lib.borrow_book(int(parts[1]), int(parts[2]))
            elif cmd == "return_book":
                lib.return_book(int(parts[1]), int(parts[2]))
            elif cmd == "check_availability":
                lib.check_availability(int(parts[1]))
            elif cmd == "display_member_books":
                lib.display_member_books(int(parts[1]))
            elif cmd == "display_library_status":
                lib.display_library_status()

