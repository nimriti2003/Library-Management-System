class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.isbn}, {self.available})"

    def checkout(self):
        if self.available:
            self.available = False
        else:
            raise Exception("Book already checked out")

    def check_in(self):
        self.available = True
