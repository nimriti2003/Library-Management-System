from datetime import datetime

class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}"

    def check_out(self):
        if self.copies > 0:
            self.copies -= 1
            return True
        else:
            return False

    def check_in(self):
        self.copies += 1

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"Name: {self.name}, User ID: {self.user_id}"

class BookManager:
    def __init__(self, storage):
        self.storage = storage
        self.books = [Book(**book) for book in self.storage.load_books()]

    def add_book(self, title, author, isbn, copies):
        book = Book(title, author, isbn, copies)
        self.books.append(book)
        self.storage.save_books(self.books)

    def list_books(self):
        return self.books

    def find_books_by_title(self, title):
        return [book for book in self.books if book.title.lower() == title.lower()]

    def find_books_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def find_books_by_isbn(self, isbn):
        return [book for book in self.books if book.isbn == isbn]

    def update_book(self, isbn, title, author, copies):
        for book in self.books:
            if book.isbn == isbn:
                book.title = title
                book.author = author
                book.copies = copies
                self.storage.save_books(self.books)
                return True
        return False

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.storage.save_books(self.books)
                return True
        return False

class UserManager:
    def __init__(self, storage):
        self.storage = storage
        self.users = [User(**user) for user in self.storage.load_users()]

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user)
        self.storage.save_users(self.users)

    def list_users(self):
        return self.users

    def find_user_by_name(self, name):
        for user in self.users:
            if user.name.lower() == name.lower():
                return user
        return None

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def update_user(self, user_id, name):
        for user in self.users:
            if user.user_id == user_id:
                user.name = name
                self.storage.save_users(self.users)
                return True
        return False

    def delete_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                self.storage.save_users(self.users)
                return True
        return False
