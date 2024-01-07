import json


def load_menu(file_path):
    try:
        with open(file_path, "r") as file:
            menu_data = json.load(file)
        return menu_data.get("books", [])
    except FileNotFoundError:
        print(f"Menu file not found: {file_path}")
        return []


def display_menu(menu):
    print("Available Books:")
    for book in menu:
        print(f"{book['title']}: ${book['price']:.2f}")


def sell_books(menu, shopping_cart):
    total_cost = 0.0

    while True:
        display_menu(menu)

        user_choice = input(
            "Enter the title of the book you want to buy (or 'done' to finish): "
        ).lower()

        if user_choice == "done":
            break
        elif any(book["title"].lower() == user_choice for book in menu):
            quantity = int(input("Enter the quantity you want to buy: "))
            if quantity > 0:
                selected_book = next(
                    book for book in menu if book["title"].lower() == user_choice
                )
                cost = selected_book["price"] * quantity
                total_cost += cost
                shopping_cart[user_choice] = (
                    shopping_cart.get(user_choice, 0) + quantity
                )
                print("\n")
                print(
                    f"Added {quantity} {user_choice}(s) to your cart. Cost: ${cost:.2f}"
                )
            else:
                print("Invalid quantity. Please enter a positive integer.")
        else:
            print("Invalid book title. Please choose a book from the list.")

        if shopping_cart:
            another_choice = input("Want to choose another book? (y/n)")
            if another_choice == "n":
                break

    return total_cost


def main():
    while True:
        print("\nWelcome to the Mbak Yul Bookstore!")
        menu_file_path = "books.json"
        menu = load_menu(menu_file_path)

        shopping_cart = {}
        print("\nMbak Yul Bookstore Ordering System")
        print("1. Buy Books")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        while choice != "2":
            if choice == "1":
                total_cost = sell_books(menu, shopping_cart)

                print("\nThank you for shopping with us!")
                print("Your Shopping Cart:")
                for title, quantity in shopping_cart.items():
                    print(f"{title.title()}: {quantity} copies")

                discount = 0
                print(f"Grand Total: ${total_cost:.2f}")
                if total_cost > 500:
                    discount += 20
                print(f"Discount: ${discount:.2f}")

                total_cost -= discount
                print(f"Total Cost: ${total_cost:.2f}")

                another_choice = input("\nWant to make another transaction? (y/n)")
                if another_choice == "n":
                    print("\nThank you for using Mbak Yul Bookstore Ordering System")
                    break

        if choice == "2":
            break

    print("Exiting the program. Goodbye!")


if __name__ == "__main__":
    main()
