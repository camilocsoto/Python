from .client import Client
from .book import Book
from dataclasses import dataclass, field
from typing import List

@dataclass
class Library():
    books: List = field(default_factory= list)
    users: List = field(default_factory= list)
    
    def add_book(self, book: Book):
        self.books.append(book)
        return f"The book {book.title} has been added to the library"
    
    def user_registry(self, user: Client):
        self.users.append(user)
        return f"{user.name} has been registered in the library"
    
    def show_books(self):
        for book in self.books:
            print(f"{book.title} is {book.is_avaliable}")