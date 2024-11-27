import mysql.connector
from datetime import datetime

# Database connection
def connect():
    return mysql.connector.connect(
        host='your_host',         # e.g., 'localhost'
        user='your_username',      # Your MySQL username
        password='your_password',  # Your MySQL password
        database='LibraryDB'       # The database name
    )

# Add a new book
def add_book(title, author, year):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO Books (title, author, year) VALUES (%s, %s, %s)"
    cursor.execute(query, (title, author, year))
    conn.commit()
    print("Book added successfully.")
    cursor.close()
    conn.close()

# Add a new member
def add_member(name, email):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO Members (name, email) VALUES (%s, %s)"
    cursor.execute(query, (name, email))
    conn.commit()
    print("Member added successfully.")
    cursor.close()
    conn.close()

# Borrow a book
def borrow_book(book_id, member_id):
    conn = connect()
    cursor = conn.cursor()
    
    # Check if the book is available
    cursor.execute("SELECT is_available FROM Books WHERE book_id = %s", (book_id,))
    result = cursor.fetchone()
    if not result or not result[0]:
        print("Book is not available.")
        return

    # Borrow the book
    borrow_date = datetime.now().date()
    query = "INSERT INTO Transactions (book_id, member_id, borrow_date) VALUES (%s, %s, %s)"
    cursor.execute(query, (book_id, member_id, borrow_date))
    cursor.execute("UPDATE Books SET is_available = %s WHERE book_id = %s", (False, book_id))
    conn.commit()
    print("Book borrowed successfully.")
    cursor.close()
    conn.close()

# Return a book
def return_book(transaction_id):
    conn = connect()
    cursor = conn.cursor()
    
    # Find book_id from the transaction
    cursor.execute("SELECT book_id FROM Transactions WHERE transaction_id = %s", (transaction_id,))
    result = cursor.fetchone()
    if not result:
        print("Transaction not found.")
        return
    
    # Return the book
    book_id = result[0]
    return_date = datetime.now().date()
    cursor.execute("UPDATE Transactions SET return_date = %s WHERE transaction_id = %s", (return_date, transaction_id))
    cursor.execute("UPDATE Books SET is_available = %s WHERE book_id = %s", (True, book_id))
    conn.commit()
    print("Book returned successfully.")
    cursor.close()
    conn.close()

# View all books
def view_books():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    for (book_id, title, author, year, is_available) in cursor:
        print(f"ID: {book_id}, Title: {title}, Author: {author}, Year: {year}, Available: {is_available}")
    cursor.close()
    conn.close()

# View all members
def view_members():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Members")
    for (member_id, name, email) in cursor:
        print(f"ID: {member_id}, Name: {name}, Email: {email}")
    cursor.close()
    conn.close()

# Main menu
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Members")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter publication year: "))
            add_book(title, author, year)
        elif choice == '2':
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            add_member(name, email)
        elif choice == '3':
            book_id = int(input("Enter book ID to borrow: "))
            member_id = int(input("Enter member ID: "))
            borrow_book(book_id, member_id)
        elif choice == '4':
            transaction_id = int(input("Enter transaction ID to return: "))
            return_book(transaction_id)
        elif choice == '5':
            view_books()
        elif choice == '6':
            view_members()
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
