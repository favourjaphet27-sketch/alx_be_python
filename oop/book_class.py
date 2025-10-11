class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that announces deletion of the book instance."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Returns a human-readable string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns an official string representation for recreating the instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
