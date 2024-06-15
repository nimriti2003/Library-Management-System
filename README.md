# Library Management System

## Overview

The Library Management System is a Python-based application designed to manage books and users in a library. It provides functionalities for adding, listing, searching, updating, and deleting books and users. Additionally, it supports checking out and checking in books. This system simplifies library operations and enhances the efficiency of managing library resources.

## Features

- Add, list, update, and delete books.
- Add, list, update, and delete users.
- Search for books by title, author, or ISBN.
- Check out and check in books.

## Installation

### Prerequisites

- Python 3.x

### Steps

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/nimriti2003/Library-Management-System.git
    cd Library-Management-System
    ```

2. **Set Up Virtual Environment (Optional but Recommended)**:
    ```sh
    python -m venv venv
    source venv/bin/activate 
    ```

3. **Install Dependencies**:
    Currently, there are no external dependencies. If you add any in the future, install them using `pip`:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Application**:
    ```sh
    python main.py
    ```

## Usage

Upon running the application, you'll be presented with a menu of options:


### Menu Options

1. **Add Book**: Adds a new book to the system.
2. **List Books**: Lists all books in the system.
3. **Find Book by Title**: Searches for books by title.
4. **Find Book by Author**: Searches for books by author.
5. **Find Book by ISBN**: Searches for books by ISBN.
6. **Update Book**: Updates the details of an existing book.
7. **Delete Book**: Deletes a book from the system.
8. **Add User**: Adds a new user to the system.
9. **List Users**: Lists all users in the system.
10. **Find User by Name**: Searches for users by name.
11. **Update User**: Updates the details of an existing user.
12. **Delete User**: Deletes a user from the system.
13. **Check Out Book**: Checks out a book to a user.
14. **Check In Book**: Checks in a book from a user.
15. **Exit**: Exits the application.

## Project Structure
Library-Management-System/
- │
- ├── books.json
- ├── main.py
- ├── book.py
- ├── user.py
- ├── models.py
- ├── check.py
- ├── storage.py
- └── README.md
