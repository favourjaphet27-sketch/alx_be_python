#!/usr/bin/python3
"""
Tests the functionality of the classes in library_system.py
"""

from library_system import Book, EBook, PrintBook, Library


def main():
    """Main function to test the library system."""
    my_library = Library()

    # Create book instances
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books
    my_library.list_books()


if __name__ == "__main__":
    main()
