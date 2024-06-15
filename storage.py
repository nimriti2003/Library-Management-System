import json

class Storage:
    def __init__(self, books_file='books.json', users_file='users.json', loans_file='loans.json'):
        self.books_file = books_file
        self.users_file = users_file
        self.loans_file = loans_file

    def load_books(self):
        try:
            with open(self.books_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_books(self, books):
        with open(self.books_file, 'w') as file:
            json.dump([book.__dict__ for book in books], file)

    def load_users(self):
        try:
            with open(self.users_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_users(self, users):
        with open(self.users_file, 'w') as file:
            json.dump([user.__dict__ for user in users], file)

    def load_loans(self):
        try:
            with open(self.loans_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_loans(self, loans):
        with open(self.loans_file, 'w') as file:
            json.dump(loans, file)
