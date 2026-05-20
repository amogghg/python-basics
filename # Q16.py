# Q16. Library Book System (Menu-driven)

print("\n" + "=" * 50)
print("Q16. Library Book System")
print("=" * 50)

library = ["Python Basics", "Data Structures", "Algorithms"]

def add_book(title):
    library.append(title)
    print(f"  Book '{title}' added.")

def remove_book(title):
    if title in library:
        library.remove(title)
        print(f"  Book '{title}' removed.")
    else:
        print(f"  Book '{title}' not found.")

def search_book(title):
    if title in library:
        print(f"  '{title}' is available.")
    else:
        print(f"  '{title}' is not available.")

def display_books():
    print("  Library books:", library)

# Demo
add_book("Machine Learning")
remove_book("Algorithms")
search_book("Python Basics")
search_book("Java")
display_books()
