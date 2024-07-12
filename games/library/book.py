class Book():
    def __init__(self, title, author):
        self.title =title
        self.author =author
        self.is_avaliable = True
        
    def borrow(self): #prestar
        if self.is_avaliable:
            self.is_avaliable = False
            return f"the book {self.title} has been borrow"
        else:
            return f"the book {self.title} has not been borrow, it's bussy"
        
    def return_book(self):
        self.is_avaliable = True