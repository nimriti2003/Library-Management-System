import json

class Storage:
    def load_books(self):
        try:
            with open('books.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_books(self, books):
        with open('books.json', 'w') as file:
            json.dump([book.__dict__ for book in books], file, indent=4)

    def load_users(self):
        try:
            with open('users.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_users(self, users):
        with open('users.json', 'w') as file:
            json.dump([user.__dict__ for user in users], file, indent=4)

    def load_loans(self):
        try:
            with open('loans.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_loans(self, loans):
        with open('loans.json', 'w') as file:
            json.dump(loans, file, indent=4)
