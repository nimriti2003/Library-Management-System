class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies  

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}), Copies: {self.copies}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "copies": self.copies
        }

    def check_out(self):
        if self.copies > 0:
            self.copies -= 1
            return True
        else:
            return False

    def check_in(self):
        self.copies += 1
