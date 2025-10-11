#!/usr/bin/python3
"""
Defines classes for a simple library system.
Includes: Book, EBook, PrintBook, and Library.
"""


class Book:
    """Base class representing a general book."""

    def __init__(self, title, author):
        """Initialize the title and author attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return string representation of a Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Subclass representing an electronic book."""

    def __init__(self, title, author, file_size):
        """Initialize attributes from Book and file_size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return string representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Subclass representing a physical print book."""

    def __init__(self, title, author, page_count):
        """Initialize attributes from Book and page_count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return string representation of a PrintBook."""
        return (
            f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
        )


class Library:
    """Class demonstrating composition by managing books."""

    def __init__(self):
        """Initialize an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)
