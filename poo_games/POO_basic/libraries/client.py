from .book import Book
from dataclasses import dataclass


@dataclass
class Client():
    name: str
    userId: int
    borrowed_books: list = None
    
    def borrow(self, book: Book): #prestar justo ahora
        if book.return_book:
            book.return_book = False
            self.borrowed_books.append(book)
            return f"{self.name} has borrowed the book {book.title}"
        else:
            return f"{self.name} could not borrow the book {book.title}"
    
    def books_returned(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            return f"{self.name} has returned the book {book.title}"