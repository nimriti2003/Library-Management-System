from book import Book
from user import User
from models import BookManager, UserManager
from check import CheckManager
from storage import Storage

def main():
    storage = Storage()
    book_manager = BookManager(storage)
    user_manager = UserManager(storage)
    check_manager = CheckManager(storage)

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Find Book by Title")
        print("4. Find Book by Author")
        print("5. Find Book by ISBN")
        print("6. Update Book")
        print("7. Delete Book")
        print("8. Add User")
        print("9. List Users")
        print("10. Find User by Name")
        print("11. Update User")
        print("12. Delete User")
        print("13. Check Out Book")
        print("14. Check In Book")
        print("15. Exit")

        choice = input("Enter choice: ").strip()

        try:
            if choice == '1':
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                isbn = input("Enter book ISBN: ").strip()
                if not title or not author or not isbn:
                    raise ValueError("Title, author, and ISBN are required.")
                book = Book(title, author, isbn)
                book_manager.add_book(book)
                print("Book added successfully.")

            elif choice == '2':
                books = book_manager.list_books()
                for book in books:
                    print(book)

            elif choice == '3':
                title = input("Enter book title to search: ").strip()
                books = book_manager.find_books_by_title(title)
                if books:
                    for book in books:
                        print(book)
                else:
                    print("No books found with that title.")

            elif choice == '4':
                author = input("Enter book author to search: ").strip()
                books = book_manager.find_books_by_author(author)
                if books:
                    for book in books:
                        print(book)
                else:
                    print("No books found by that author.")

            elif choice == '5':
                isbn = input("Enter book ISBN to search: ").strip()
                books = book_manager.find_books_by_isbn(isbn)
                if books:
                    for book in books:
                        print(book)
                else:
                    print("No books found with that ISBN.")

            elif choice == '6':
                isbn = input("Enter book ISBN to update: ").strip()
                title = input("Enter new title (leave blank to keep current): ").strip()
                author = input("Enter new author (leave blank to keep current): ").strip()
                if book_manager.update_book(isbn, title, author):
                    print("Book updated successfully.")
                else:
                    print("Book not found.")

            elif choice == '7':
                isbn = input("Enter book ISBN to delete: ").strip()
                if book_manager.delete_book(isbn):
                    print("Book deleted successfully.")
                else:
                    print("Book not found.")

            elif choice == '8':
                name = input("Enter user name: ").strip()
                user_id = input("Enter user ID: ").strip()
                if not name or not user_id:
                    raise ValueError("Name and user ID are required.")
                user = User(user_id, name)
                user_manager.add_user(user)
                print("User added successfully.")

            elif choice == '9':
                users = user_manager.list_users()
                for user in users:
                    print(user)

            elif choice == '10':
                name = input("Enter user name to search: ").strip()
                users = user_manager.find_user_by_name(name)
                for user in users:
                    print(user)

            elif choice == '11':
                user_id = input("Enter user ID to update: ").strip()
                name = input("Enter new name (leave blank to keep current): ").strip()
                if user_manager.update_user(user_id, name):
                    print("User updated successfully.")
                else:
                    print("User not found.")

            elif choice == '12':
                user_id = input("Enter user ID to delete: ").strip()
                if user_manager.delete_user(user_id):
                    print("User deleted successfully.")
                else:
                    print("User not found.")

            elif choice == '13':
                user_id = input("Enter user ID for checkout: ").strip()
                isbn = input("Enter book ISBN for checkout: ").strip()
                user = user_manager.find_user_by_id(user_id)
                books = book_manager.find_books_by_isbn(isbn)
                if user and books:
                    check_manager.checkout_book(user, books[0])
                else:
                    print("User or Book not found.")

            elif choice == '14':
                user_id = input("Enter user ID for checkin: ").strip()
                isbn = input("Enter book ISBN for checkin: ").strip()
                user = user_manager.find_user_by_id(user_id)
                books = book_manager.find_books_by_isbn(isbn)
                if user and books:
                    check_manager.check_in_book(user, books[0])
                else:
                    print("User or Book not found.")

            elif choice == '15':
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
