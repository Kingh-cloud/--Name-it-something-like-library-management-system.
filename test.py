# Import your library system functions here if needed
# from library_system import *

# Clear data before testing
books.clear()
members.clear()

# Test 1: Add a book
print("Test 1: Add Book")
result = add_book("12345", "The Time Machine", "H.G. Wells", "Sci-Fi", 5)
assert result == "Book added successfully.", result
print("✓ Book added")

# Test 2: Add the same book again
print("Test 2: Add Duplicate Book")
result = add_book("12345", "The Time Machine", "H.G. Wells", "Sci-Fi", 5)
assert result == "Book already exists.", result
print("✓ Duplicate book check passed")

# Test 3: Add a member
print("Test 3: Add Member")
result = add_member("M001", "Alice", "alice@example.com")
assert result == "Member added successfully.", result
print("✓ Member added")

# Test 4: Borrow a book
print("Test 4: Borrow Book")

result = borrow_book("M001", "12345")
assert result == "Book borrowed successfully.", result
print("✓ Book borrowed")

# Test 5: Return the book
print("Test 5: Return Book")
result = return_book("M001", "12345")
assert result == "Book returned successfully.", result
print("✓ Book returned")

# Test 6: Search for a book
print("Test 6: Search Book")
results = search_books("Time")
assert len(results) == 1 and results[0][0] == "12345", results
print("✓ Book search successful")

# Test 7: Update book genre
print("Test 7: Update Book")
result = update_book("12345", genre="Fantasy")
assert result == "Book updated successfully.", result
print("✓ Book updated")

# Test 8: Delete member with no borrowed books
print("Test 8: Delete Member")
result = delete_member("M001")
assert result == "Member deleted successfully.", result
print("✓ Member deleted")

# Test 9: Delete book
print("Test 9: Delete Book")
result = delete_book("12345")
assert result == "Book deleted successfully.", result
print("✓ Book deleted")

print("\n🎉 All tests passed!")


