from operations import add_book, add_member, borrow_book, return_book, delete_book

# Setup sample data
books = {}
members = []
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Fantasy", "Biography")

# Test 1: Add a valid book
assert add_book("978-1111111111", "Test Book", "Test Author", "Fiction", 2) == "Book added successfully."

# Test 2: Add a duplicate book
assert add_book("978-1111111111", "Test Book", "Test Author", "Fiction", 2) == "Book already exists."

# Test 3: Add a valid member
assert add_member("M100", "Bob", "bob@example.com") == "Member added successfully."

# Test 4: Borrow a book successfully
assert borrow_book("M100", "978-1111111111") == "Book borrowed successfully."

# Test 5: Borrow when no copies left
borrow_book("M100", "978-1111111111")  # second copy
assert borrow_book("M100", "978-1111111111") == "Book not available."

from operations import *

# Add genres (already defined globally)
print("Genres:", genres)

# Add books
print(add_book("978-2222222222", "Python Basics", "Jane Doe", "Non-Fiction", 3))
print(add_book("978-3333333333", "Sci-Fi World", "John Smith", "Sci-Fi", 1))

# Add members
print(add_member("M001", "Alice Smith", "alice@example.com"))
print(add_member("M002", "Bob Jones", "bob@example.com"))

# Search books
print("Search results for 'Python':", search_books("Python"))

# Borrow books
print(borrow_book("M001", "978-2222222222"))
print(borrow_book("M001", "978-3333333333"))

# Return a book
print(return_book("M001", "978-2222222222"))

# Try deleting a borrowed book
print(delete_book("978-3333333333"))  # Should fail

# Delete a member with no borrowed books
print(delete_member("M002"))  # Should succeed



