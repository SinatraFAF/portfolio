# Import the SQLite
import sqlite3

# This portion of the code is a function which
# will be used in other functions to connect to
# the database and create a cursor object


def connect():
    try:
        # Create the database to manage inventory
        db = sqlite3.connect('ebookstore.db')

        # Enable foreign keys
        db.execute("PRAGMA foreign_keys = ON")

        # Create a cursor object
        cursor = db.cursor()

        # Return db and cursor
        return db, cursor

    # This is the except error and it's message
    except sqlite3.Error:
        print("Unable to connect to database")
        return None, None

# Define a function to create the book table and populate it


def create_book_table():
    # Call the function to access the database and cursor object
    # and check that the database can be connected to
    # This is done at the beginning of all subsequent functions
    db, cursor = connect()
    if db is None:
        return

    # Create the table
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS book(
        id INTEGER PRIMARY KEY, 
        title TEXT, 
        authorID INTEGER,
        qty INTEGER)
    ''')

    # Commit change (This will be done after every change
    # to confirm the changes)
    db.commit()

    # Insert the books which we already have into the table
    book_data = [
        (3001, "A Tale of Two Cities", 1290, 30),
        (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
        (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
        (3004, "The Lord of the Rings", 6380, 37),
        (3005, "Alice's Adventures in Wonderland", 5620, 12)
    ]
    cursor.executemany(
        '''
        INSERT OR IGNORE INTO book(id, title, authorID, qty)
        VALUES(?, ?, ?, ?)
        ''',
        book_data
    )

    db.commit()
    db.close()  # This closes the connection to the database

# Define the function to create the author table and populate it


def create_author_table():
    db, cursor = connect()
    if db is None:
        return
    # Insert a new table into the database
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS author(
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        country TEXT)
        '''
    )

    db.commit()

    # Create a list with author data
    author_data = [(1290, "Charles Dickens", "England"),
                   (8937, "J.K. Rowling", "England"),
                   (2356, "C.S. Lewis", "Ireland"),
                   (6380, "J.R.R. Tolkien", "South Africa"),
                   (5620, "Lewis Carroll", "England")
                   ]

    # Insert the list into the author table
    cursor.executemany(
        '''
        INSERT OR IGNORE INTO author (id, name, country)
        VALUES(?, ?, ?)
        ''',
        author_data
    )

    db.commit()
    db.close()

# Define helper function for getting valid numbers from the user


def valid_num(prompt):
    while True:
        value = input(prompt).strip()

        # This ensures only digits are accepted
        if not value.isdigit():
            print("Please enter numbers.")
            continue

        # This ensures it must be 4 digits
        if len(value) != 4:
            print("Input should be 4 digits.")
            continue

        return int(value)


# Define function to add book


def add_book():
    db, cursor = connect()
    if db is None:
        return

    try:
        book_id = valid_num("\nWhat is the ID of the book?: ")
        title = input("What is the title of the book?: ")
        author_id = valid_num("What is the author ID of the book?: ")
        qty = int(input("What is the quantity of the book?: "))
        author_name = input("What is the author's name?: ")
        author_country = input("Which country is the author from?: ")

        cursor.execute(
            '''
            INSERT INTO book(id, title, authorID, qty)
            VALUES(?, ?, ?, ?)
            ''', (book_id, title, author_id, qty)
        )

        db.commit()

        cursor.execute(
            '''
            INSERT INTO author(id, name, country)
            VALUES(?, ?, ?)
            ''', (author_id, author_name, author_country)
        )

        db.commit()
        print("Book added.\n")

    except sqlite3.IntegrityError:
        print("Please try another book ID or author ID.")

    except sqlite3.Error:
        print("There was an error with the database.")

    finally:
        db.close()


# Define the function to be used in update_book which will
# allow the user to update book information


def update_book_info(cursor, book_id, title, qty):
    print("\nCurrent book details:")
    print(f"Title: {title}")
    print(f"Quantity: {qty}\n")

    new_title = input("New title (Enter for no change): ")
    new_qty = input("New quantity (Enter for no change): ")

    if new_title.strip() == "":
        new_title = title

    if new_qty.strip() == "":
        new_qty = qty
    else:
        # This logic checks that the input is a number
        if not new_qty.isdigit():
            print("Invalid input. No change.")
            new_qty = qty

        else:
            new_qty = int(new_qty)

    cursor.execute(
        '''
        UPDATE book SET title = ?, qty = ?
        WHERE id = ?
        ''', (new_title, new_qty, book_id)
    )

# Define the function to be used in update_book which will
# allow the user to update author information


def update_author_info(cursor, author_id, name, country):
    print("\nCurrent author details:")
    print(f"Author name: {name}")
    print(f"Author country: {country}\n")

    new_name = input("New author name (Enter for no change): ")
    new_country = input("New author country (Enter for no change): ")

    if new_name.strip() == "":
        new_name = name

    if new_country.strip() == "":
        new_country = country

    cursor.execute(
        '''
        UPDATE author SET name = ?, country = ?
        WHERE id = ?
        ''', (new_name, new_country, author_id)
    )

# Define the function to update a book


def update_book():
    db, cursor = connect()
    if db is None:
        return

    book_id = valid_num("Please enter the ID of the book to update: ")

    cursor.execute(
        '''
        SELECT book.id, book.title, book.qty, 
        author.id, author.name, author.country FROM BOOK
        JOIN author ON book.authorID = author.id 
        WHERE book.id = ?
        ''', (book_id,)
    )

    result = cursor.fetchone()

    if result is None:
        print("No book found for this ID.\n")
        db.close()
        return

    book_id, title, qty, author_id, name, country = result

    # Call the functions to update book and author
    update_book_info(cursor, book_id, title, qty)
    update_author_info(cursor, author_id, name, country)

    db.commit()
    db.close()

    print("\nBook information saved.\n")

# Define the function to delete a book


def delete_book():
    db, cursor = connect()
    if db is None:
        return

    book_id = valid_num("Please enter the ID of the book to delete: ")

    # This logic checks that the book exists in the database
    cursor.execute(
        '''
        SELECT id FROM book WHERE id = ?
        ''', (book_id,)
    )

    if cursor.fetchone() is None:
        print("There is no book with that ID.\n")
        db.close()
        return

    # Ask the user to confirm that they want to delete the book
    confirm = input("Are you sure (y/n): ")
    if confirm.lower() != "y":
        print("No book deleted.\n")
        db.close()
        return

    try:
        cursor.execute(
            '''
            DELETE FROM book WHERE id = ?
            ''', (book_id,)
        )

        db.commit()
        print("Book deleted.\n")

    except sqlite3.Error:
        print("There was an error with the database.")

    finally:
        db.close()

# Define the function to search for a book


def search_book():
    db, cursor = connect()
    if db is None:
        return

    book_id = valid_num("Please enter the ID of the book to find: ")

    cursor.execute(
        '''
        SELECT book.title, author.name, book.qty FROM book
        JOIN author ON book.authorID = author.id
        WHERE book.id = ?
        ''', (book_id,)
    )

    result = cursor.fetchone()

    if result is None:
        print("No book found for this ID.\n")
        db.close()
        return

    title, author, qty = result

    print(f"\nTitle: {title}")
    print(f"Author: {author}")
    print(f"Quantity: {qty}")

    db.close()

# Define the function to view all books


def view_all():
    db, cursor = connect()
    if db is None:
        return

    # Get book and author info from database
    cursor.execute(
        '''
        SELECT book.title, author.name, author.country FROM book
        JOIN author ON book.authorID = author.id
        '''
    )

    results = cursor.fetchall()

    headers = ["Title", "Author's Name", "Author's country"]

    print("\nDetails")
    print("-" * 60)

    # Print each book's information
    for row in results:
        for header, value in zip(headers, row):
            print(f"{header}: {value}")
        print("-" * 60)

    db.close()


# The following functions are called to load the tables
# for the user to interact with
create_book_table()
create_author_table()

# This is the menu the user will interact with
while True:
    try:
        print("Bookstore Inventory Manager\n")
        print("Please select one of the following options:")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search book")
        print("5. View all books")
        print("0. Exit")

        choice = int(input("Select an option here: "))

        if choice == 1:
            add_book()

        elif choice == 2:
            update_book()

        elif choice == 3:
            delete_book()

        elif choice == 4:
            search_book()

        elif choice == 5:
            view_all()

        elif choice == 0:
            print("End")
            break

    except ValueError:
        print("Please provide a valid choice")
