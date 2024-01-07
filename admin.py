import json


def load_books(file_path):
    try:
        with open(file_path, "r") as file:
            books_data = json.load(file)
        return books_data.get("books", [])
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


def save_books(books, file_path):
    with open(file_path, "w") as file:
        json.dump({"books": books}, file, indent=2)


def display_books(books):
    if not books:
        print("No books available.")
    else:
        print("Available Books:")
        for book in books:
            print(
                f"ID: {book['id']}, Title: {book['title']} Price: ${book['price']:.2f}"
            )


def add_book(books, file_path):
    new_book = {}
    duplicatedID = True

    while duplicatedID:
        new_book["id"] = input("Enter the book ID: ")
        duplicatedID = False
        for book in books:
            if book["id"] == new_book["id"]:
                print("\nID already used for another book!")
                duplicatedID = True

    new_book["title"] = input("Enter the book title: ")
    new_book["price"] = float(input("Enter the book price: "))

    books.append(new_book)
    save_books(books, file_path)
    print("Book added successfully.")


def update_book(books, file_path):
    book_id = input("Enter the ID of the book to update: ")
    for book in books:
        if book["id"] == book_id:
            book["title"] = input("Enter the new title: ")
            book["price"] = float(input("Enter the new price: "))
            save_books(books, file_path)
            print("\nBook updated successfully.")

            another_choice = input("Want to update another book? (y)")
            if another_choice == "y":
                update_book(books, file_path)

            return
    print(f"No book found with ID {book_id}.")


def delete_book(books, file_path):
    book_id = input("Enter the ID of the book to delete: ")
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_books(books, file_path)
            print("\nBook deleted successfully.")

            another_choice = input("Want to delete another book? (y)")
            if another_choice == "y":
                delete_book(books, file_path)

            return
    print(f"No book found with ID {book_id}.")


def main():
    file_path = "books.json"
    books = load_books(file_path)

    while True:
        print("\nBookshop Management System")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_books(books)
        elif choice == "2":
            add_book(books, file_path)
        elif choice == "3":
            update_book(books, file_path)
        elif choice == "4":
            delete_book(books, file_path)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
