from datetime import datetime

class CheckManager:
    def __init__(self, storage):
        self.storage = storage
        self.loans = self.storage.load_loans()
        
    def checkout_book(self, user, book):
        if not book.available:
            raise Exception("Book is already checked out.")
        book.checkout()
        self.loans.append({
            'user_id': user.user_id,
            'isbn': book.isbn,
            'checkout_date': str(datetime.now())
        })
        self.storage.save_loans(self.loans)
        print(f"Book {book.title} checked out by {user.name}.")

    def check_in_book(self, user, book):
        book.check_in()
        self.loans = [loan for loan in self.loans if not (loan['user_id'] == user.user_id and loan['isbn'] == book.isbn)]
        self.storage.save_loans(self.loans)
        print(f"Book {book.title} checked in by {user.name}.")
