import json

file = "library_data.json"

books = []

def load_data():
    try:
        with open(file, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return []


def save_data():
    with open(file, "w") as f:
        json.dump(books, f, indent=4)


def add_book(books):
    book = input("Enter the book name: ")
    book_id = int(input("Enter the book id: "))

    book_data = {
        "name": book,
        "id": book_id
    }

    books.append(book_data)

    save_data()

    print("Book added successfully!")


def view_books(books):

    if not books:
        print("There are no books!")
        return

    print("\n===== BOOKS =====")

    for book in books:
        print(f"ID: {book['id']} | Name: {book['name']}")


def search_books(books):

    search_book = input("Search the book: ").lower()

    for book in books:
        if search_book in book["name"].lower():
            print(
                f"ID: {book['id']} | "
                f"Name: {book['name']}"
            )
            return

    print("This book is not available.")


def delete_book(books):

    delete_id = int(input("Enter book ID to delete: "))

    for book in books:
        if book["id"] == delete_id:
            books.remove(book)
            save_data()

            print("Book deleted successfully!")
            return

    print("This book is not in the list.")


# Load saved books when program starts
books = load_data()


while True:

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1) Add Book")
    print("2) View Books")
    print("3) Search Book")
    print("4) Delete Book")
    print("5) Exit")

    choice = int(input("Enter the number: "))

    if choice == 1:
        add_book(books)

    elif choice == 2:
        view_books(books)

    elif choice == 3:
        search_books(books)

    elif choice == 4:
        delete_book(books)

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid Number! Please Enter Valid Number.")





    

    










