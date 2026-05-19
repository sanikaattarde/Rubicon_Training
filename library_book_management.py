# Library Book Management (Do not use class) (use list,loop statement, functions, Operators)

# Create a list of books in the library (Store details like: Book ID, Title, Author, Quantity) 
books = [ "Hello", "Mello"," Multiverse of Pranav", "Group" ]


# function to display available books
def display_books():
    print("Available books in the library:")
    for book in books:
        print(book)

# function to add a new book to the library (use concatenation)
def add_book(book):
    books.append(book)
    print("Book added: " + book)


# function to remove a book from the library
def remove_book(book):
    if book in books:
        books.remove(book)
        print("Book removed: " + book)
    else:
        print("Book not found in the library.")

# function to search for a book in the library
def search_book(book):
    if book in books:
        print("Book found: " + book)
    else:
        print("Book not found in the library.")
        


# Main program
while True:
    print("Library Book Management System")
    print("1. Display available books")
    print("2. Add a new book")
    print("3. Remove a book")
    print("4. Search for a book")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        display_books()
    elif choice == '2':
        new_book = input("Enter the name of the book to add: ")
        add_book(new_book)
    elif choice == '3':
        book_to_remove = input("Enter the name of the book to remove: ")
        remove_book(book_to_remove)
    elif choice == '4':
        book_to_search = input("Enter the name of the book to search: ")
        search_book(book_to_search)
    elif choice == '5':
        print("Exiting the System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        



