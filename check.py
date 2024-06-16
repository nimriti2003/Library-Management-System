import json
from datetime import datetime

class CheckManager:
    def __init__(self, storage, book_manager, user_manager):
        self.storage = storage
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.checkouts = self.storage.load_loans()

    def check_out_book(self, user_id, isbn):
        book = self.book_manager.find_books_by_isbn(isbn)
        user = self.user_manager.find_user_by_id(user_id)

        if book and user:
            book = book[0]
            if book.check_out():
                checkout_time = datetime.now().isoformat()
                self.checkouts.append({"user_id": user_id, "isbn": isbn, "checkout_time": checkout_time})
                self.book_manager.storage.save_books(self.book_manager.books)
                self.storage.save_loans(self.checkouts)
                return True
        return False

    def check_in_book(self, user_id, isbn):
        book = self.book_manager.find_books_by_isbn(isbn)
        user = self.user_manager.find_user_by_id(user_id)

        if book and user:
            book = book[0]
            for checkout in self.checkouts:
                if checkout["user_id"] == user_id and checkout["isbn"] == isbn:
                    book.check_in()
                    self.checkouts.remove(checkout)
                    self.book_manager.storage.save_books(self.book_manager.books)
                    self.storage.save_loans(self.checkouts)
                    return True
        return False

    def list_checkouts(self):
        return self.checkouts
