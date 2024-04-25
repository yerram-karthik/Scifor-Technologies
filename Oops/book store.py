class Book:
    def __init__(self, book_id, title, price):
        self.book_id = book_id
        self.title = title
        self.price = price

class BookStore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def get_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def get_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def get_book_by_price(self, price):
        for book in self.books:
            if book.price == price:
                return book
        return None

    def show_all_books(self):
        if self.books:
            print("List of Books in the Store:")
            for book in self.books:
                print(f"ID: {book.book_id}, Title: {book.title}, Price: {book.price}")
        else:
            print("No books in the store.")

    def delete_book(self, identifier):
        for book in self.books:
            if book.book_id == identifier or book.title == identifier or book.price == identifier:
                self.books.remove(book)
                print("Book deleted successfully!")
                return
        print("Book not found.")

def main():
    store = BookStore()

    while True:
        print("\nOptions:")
        print("1. Add a new book")
        print("2. Get a book by ID")
        print("3. Get a book by title")
        print("4. Get a book by price")
        print("5. Show all books")
        print("6. Delete a book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter the book ID: ")
            title = input("Enter the title of the book: ")
            price = input("Enter the price of the book: ")
            new_book = Book(book_id, title, price)
            store.add_book(new_book)
        elif choice == '2':
            book_id = input("Enter the book ID: ")
            book = store.get_book_by_id(book_id)
            if book:
                print(f"Book found: Title - {book.title}, Price - {book.price}")
            else:
                print("Book not found.")
        elif choice == '3':
            title = input("Enter the title of the book: ")
            book = store.get_book_by_title(title)
            if book:
                print(f"Book found: ID - {book.book_id}, Price - {book.price}")
            else:
                print("Book not found.")
        elif choice == '4':
            price = input("Enter the price of the book: ")
            book = store.get_book_by_price(price)
            if book:
                print(f"Book found: ID - {book.book_id}, Title - {book.title}")
            else:
                print("Book not found.")
        elif choice == '5':
            store.show_all_books()
        elif choice == '6':
            identifier = input("Enter the book ID, title, or price to delete: ")
            store.delete_book(identifier)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
