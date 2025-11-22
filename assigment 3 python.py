library-inventory-manager-MANOJ KUMAR/
│
├── library_manager/
│   ├── __init__.py
│   ├── book.py
│   ├── inventory.py
│
├── cli/
│   └── main.py
│
├── catalog.json
├── README.md
├── requirements.txt
└── .gitignore


class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Status: {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        return self.status == "available"


import json
from pathlib import Path
from .book import Book
import logging

logging.basicConfig(filename="library.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class LibraryInventory:
    def __init__(self, file_path="catalog.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_data()

    def load_data(self):
        try:
            if self.file_path.exists():
                with open(self.file_path, "r") as f:
                    data = json.load(f)
                    for item in data:
                        self.books.append(Book(**item))
            else:
                self.save_data()
        except Exception as e:
            logging.error("Error loading file: %s", e)
            print("Error loading catalog. Starting with an empty library.")

    def save_data(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)
        except Exception as e:
            logging.error("Error saving file: %s", e)

    def add_book(self, book):
        self.books.append(book)
        self.save_data()
        logging.info("Book added: %s", book.title)

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        return self.books



from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def menu():
    print("\n===== LIBRARY INVENTORY MANAGER =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def main():
    inventory = LibraryInventory()

    while True:
        menu()
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if choice == 1:
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            inventory.add_book(book)
            print("Book added successfully!")

        elif choice == 2:
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save_data()
                print("Book issued!")
            else:
                print("Book not found or already issued.")

        elif choice == 3:
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.return_book():
                inventory.save_data()
                print("Book returned!")
            else:
                print("Book not found or not issued.")

        elif choice == 4:
            all_books = inventory.display_all()
            for b in all_books:
                print(b)

        elif choice == 5:
            title = input("Enter title to search: ")
            results = inventory.search_by_title(title)
            if results:
                for b in results:
                    print(b)
            else:
                print("No books found.")

        elif choice == 6:
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
