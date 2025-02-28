class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __repr__(self):
        return f"To nowa książka pt. {self.title}, autorstwa {self.author}, opublikowana w roku {self.publication_year}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)


if __name__ == "__main__":
    library = Library()

    while True:
        action = input("Choose an action: [1] Add book [2] Show books [3] Exit: ")

        if action == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            publication_year = input("Enter publication year: ")
            new_book = Book(title, author, publication_year)
            library.add_book(new_book)
            print(f"Book '{title}' added to the library.")

        elif action == "2":
            print("Books in the library:")
            library.show_books()

        elif action == "3":
            print("Exiting...")
            break
        else:
            print("Invalid action. Please try again.")