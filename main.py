from models import BookManager, UserManager
from check import CheckManager
from storage import Storage

def main():
    storage = Storage()
    book_manager = BookManager(storage)
    user_manager = UserManager(storage)
    check_manager = CheckManager(storage, book_manager, user_manager)

    while True:
        print("Library Management System")
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
        print("15. List Checkouts")
        print("16. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            copies = int(input("Enter number of copies: "))
            book_manager.add_book(title, author, isbn, copies)
        elif choice == '2':
            books = book_manager.list_books()
            for book in books:
                print(book)
        elif choice == '3':
            title = input("Enter book title to search: ")
            books = book_manager.find_books_by_title(title)
            if books:
                for book in books:
                    print(book)
            else:
                print("Book not found.")
        elif choice == '4':
            author = input("Enter book author to search: ")
            books = book_manager.find_books_by_author(author)
            if books:
                for book in books:
                    print(book)
            else:
                print("Book not found.")
        elif choice == '5':
            isbn = input("Enter book ISBN to search: ")
            books = book_manager.find_books_by_isbn(isbn)
            if books:
                for book in books:
                    print(book)
            else:
                print("Book not found.")
        elif choice == '6':
            isbn = input("Enter book ISBN to update: ")
            title = input("Enter new book title: ")
            author = input("Enter new book author: ")
            copies = int(input("Enter new number of copies: "))
            updated = book_manager.update_book(isbn, title, author, copies)
            if updated:
                print("Book updated.")
            else:
                print("Book not found.")
        elif choice == '7':
            isbn = input("Enter book ISBN to delete: ")
            deleted = book_manager.delete_book(isbn)
            if deleted:
                print("Book deleted.")
            else:
                print("Book not found.")
        elif choice == '8':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(name, user_id)
        elif choice == '9':
            users = user_manager.list_users()
            for user in users:
                print(user)
        elif choice == '10':
            name = input("Enter user name to search: ")
            user = user_manager.find_user_by_name(name)
            if user:
                print(user)
            else:
                print("User not found.")
        elif choice == '11':
            user_id = input("Enter user ID to update: ")
            name = input("Enter new user name: ")
            updated = user_manager.update_user(user_id, name)
            if updated:
                print("User updated.")
            else:
                print("User not found.")
        elif choice == '12':
            user_id = input("Enter user ID to delete: ")
            deleted = user_manager.delete_user(user_id)
            if deleted:
                print("User deleted.")
            else:
                print("User not found.")
        elif choice == '13':
            user_id = input("Enter user ID for checkout: ")
            isbn = input("Enter book ISBN for checkout: ")
            checked_out = check_manager.check_out_book(user_id, isbn)
            if checked_out:
                print("Book checked out successfully.")
            else:
                print("Checkout failed. Book might not be available or user not found.")
        elif choice == '14':
            user_id = input("Enter user ID for check-in: ")
            isbn = input("Enter book ISBN for check-in: ")
            checked_in = check_manager.check_in_book(user_id, isbn)
            if checked_in:
                print("Book checked in successfully.")
            else:
                print("Check-in failed. Book or user not found.")
        elif choice == '15':
            checkouts = check_manager.list_checkouts()
            for checkout in checkouts:
                print(f"User ID: {checkout['user_id']}, ISBN: {checkout['isbn']}, Checkout Time: {checkout['checkout_time']}")
        elif choice == '16':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
