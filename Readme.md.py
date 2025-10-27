books = {
    "978-1234567890": {
        "title": "Book Title",
        "author": "Author Name",
        "genre": "Fiction",
        "total_copies": 5
    },
}
members = [
    {
        "member_id": "M001",
        "name": "Alice Smith",
        "email": "alice@example.com",
        "borrowed_books": ["978-1234567890", "978-0987654321"]
    },
    ...
]
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Fantasy", "Biography")
books = {}
members = []
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Fantasy", "Biography")
def add_book(isbn, title, author, genre, total_copies):