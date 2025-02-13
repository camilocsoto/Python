from libraries import Book
from libraries import Client
from libraries import Library

if __name__ == "__main__":
    library = Library()
    
    book1 = Book("The Lord of the Rings", "J.R.R. Tolkien")
    library.add_book(book1)
    
    user1 = Client("Gandalf", 10012312)
    library.user_registry(user1)
    
    library.show_books()
    
    