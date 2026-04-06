books = []

def add_book():
    book = input("Enter book name to add: ")
    books.append(book)
    print(book, "added successfully.")


def issue_book():
    book = input("Enter book name to issue: ")
    if book in books:
        books.remove(book)
        print(book, "issued successfully")
    else:
        print("Book not available")


def return_book():
    book = input("Enter book name to return: ")
    books.append(book)
    print(book, "returned successfully")


def available_books():
    book = input("Enter book name to return: ")
    if book in books:
        print("book is availabe")
    else:
        print("book is not available")
        print(books,"this are available books")



while True:
    print("Library System")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Available Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        issue_book()
    elif choice == 3:
        return_book()
    elif choice == 4:
        available_books()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice\n")



















