from storage import Storage
from book import Book
from user import User

class BookManager:
    def __init__(self, storage):
        self.storage = storage
        self.books = [Book(**book) for book in self.storage.load_books()]

    def add_book(self, book):
        self.books.append(book)
        self.storage.save_books(self.books)

    def list_books(self):
        return self.books

    def find_books_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def find_books_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

    def find_books_by_isbn(self, isbn):
        return [book for book in self.books if book.isbn == isbn]

    def update_book(self, isbn, title=None, author=None):
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                self.storage.save_books(self.books)
                return True
        return False

    def delete_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self.storage.save_books(self.books)

class UserManager:
    def __init__(self, storage):
        self.storage = storage
        self.users = [User(**user) for user in self.storage.load_users()]

    def add_user(self, user):
        self.users.append(user)
        self.storage.save_users(self.users)

    def list_users(self):
        return self.users

    def find_user_by_name(self, name):
        return [user for user in self.users if name.lower() in user.name.lower()]

    def find_user_by_id(self, user_id):
        return next((user for user in self.users if user.user_id == user_id), None)

    def update_user(self, user_id, name=None):
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                self.storage.save_users(self.users)
                return True
        return False

    def delete_user(self, user_id):
        self.users = [user for user in self.users if user.user_id != user_id]
        self.storage.save_users(self.users)
