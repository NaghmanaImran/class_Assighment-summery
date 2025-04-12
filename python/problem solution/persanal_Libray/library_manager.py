import json
import os

data_file = 'library.txt'

def load_library():
    """Loads the library from a file if it exists; otherwise, returns an empty list."""
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    """Saves the library data to a file."""
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Adds a new book to the library."""
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read the book? (yes/no): ').strip().lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(new_book)
    save_library(library)
    print(f'Book "{title}" added successfully.')

def remove_book(library):
    """Removes a book from the library by title."""
    title = input("Enter the title of the book to remove: ").strip().lower()

    initial_length = len(library)
    updated_library = [book for book in library if book['title'].lower() != title]

    if len(updated_library) < initial_length:
        save_library(updated_library)
        print(f'Book "{title}" removed successfully.')
    else:
        print(f'Book "{title}" not found in the library.')

    return updated_library  # Ensure the updated library is returned

def search_library(library):
    """Search for books by title or author."""
    search_by = input("Search by title or author: ").strip().lower()
    if search_by not in ['title', 'author']:
        print("Invalid choice. Please enter 'title' or 'author'.")
        return

    search_term = input(f"Enter the {search_by}: ").strip().lower()

    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        print("\n📚 Search Results 📚")
        for book in results:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print(f"No books found matching '{search_term}' in the {search_by} field.")

def display_all_books(library):
    """Display all books in the library."""
    if library:
        print("\n📚 Library Collection 📚")
        for book in library:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print("The library is empty.")

def display_statistics(library):
    """Displays statistics about the library."""
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print("\n📊 Library Statistics 📊")
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def main():
    library = load_library()
    
    while True:
        print("\n📖 Welcome to the Library Manager 📖")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search the library")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            library = remove_book(library)  # ✅ Fix: Update library after removing a book
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("📚 Goodbye! Have a great day! 📚")
            break  # Exit the loop
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
