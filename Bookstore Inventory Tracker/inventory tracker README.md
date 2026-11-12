# ShelfTrack: Bookstore Inventory System

A command-line application that lets a bookstore clerk manage book inventory and author details, backed by a relational SQLite database.

## Problem Statement

A bookstore needs a simple, reliable way to track stock. The clerk must be able to add, update, delete, and look up books, and see each book alongside its author's details. This project implements that as a menu-driven Python program on a two-table relational database, with validation and error handling so that bad input cannot corrupt the data.

## Database

- **Engine:** SQLite (`ebookstore`)
- **Tables:** `book` and `author`, linked by a foreign key
- **Starter data:** populated on first run with the provided records

### Schema

**book**

| Column   | Description                         |
|----------|-------------------------------------|
| id       | Primary key (four-digit integer)    |
| title    | Book title                          |
| authorID | Foreign key referencing `author.id` |
| qty      | Quantity in stock                   |

**author**

| Column  | Description                       |
|---------|-----------------------------------|
| id      | Primary key (four-digit integer)  |
| name    | Author's name                     |
| country | Author's country                  |

## Features

```
1. Enter book
2. Update book
3. Delete book
4. Search books
5. View details of all books
0. Exit
```

- **Enter book:** add a new book record
- **Update book:** defaults to updating quantity; title or author ID can be selected to correct a record. The current author name and country are shown and can be edited and saved
- **Delete book:** remove a book by ID
- **Search books:** find a specific book
- **View details of all books:** displays title, author name, and author country, using an `INNER JOIN` across both tables

Example output for option 5:

```
Details --------------------------------------------------
Title: The Tale of Two Cities
Author's Name: Charles Dickens
Author's Country: England
---------------------------------------------------
```

## Approach

### Database Setup
- Functions to create the database connection and the `book` and `author` tables
- Tables populated with starter data on first run

### Querying
- `INNER JOIN` on `book.authorID = author.id` to retrieve book and author columns in a single query
- Parameterised queries throughout, so user input is never concatenated into SQL

### Validation and Error Handling
- Book and author IDs must be integers with exactly four digits
- Menu choices and other inputs are checked before use
- `try/except` blocks handle invalid input and database errors, with user-friendly messages

### Resource Management
- Database connections are handled with context managers (`with` statements) so they close automatically

## Code Quality

- **Modularity:** separate functions for database operations and for each menu action
- **Naming and refactoring:** descriptive names, with redundant code removed
- **Documentation and style:** docstrings and comments, PEP 8 compliant
- **Testing:** each menu option tested with valid and invalid input

## Key Concepts Demonstrated

- CRUD operations in SQL
- Relational design with primary and foreign keys
- `INNER JOIN` across tables
- SQL injection prevention with parameterised queries
- Input validation and exception handling in Python
- Modular, maintainable code structure

## Tech Stack

- Python 3
- SQLite (`sqlite3`)

## How to Run

Simply download and run the programme
