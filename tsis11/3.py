import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

# Create a table to store the phonebook data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS phonebook (
        id INTEGER PRIMARY KEY,
        user_name TEXT,
        phone_number TEXT
    )
''')
conn.commit()

# Function to return records based on a pattern
def search_records(pattern):
    cursor.execute('''
        SELECT * FROM phonebook
        WHERE user_name LIKE ? OR phone_number LIKE ?
    ''', ('%'+pattern+'%', '%'+pattern+'%'))
    return cursor.fetchall()

# Procedure to insert or update a user
def insert_or_update_user(user_name, phone_number):
    cursor.execute('''
        INSERT OR REPLACE INTO phonebook (user_name, phone_number)
        VALUES (?, ?)
    ''', (user_name, phone_number))
    conn.commit()

# Procedure to insert many new users
def insert_many_users(users):
    for user in users:
        insert_or_update_user(user['user_name'], user['phone_number'])

# Function to query data with pagination
def query_with_pagination(limit, offset):
    cursor.execute('''
        SELECT * FROM phonebook
        LIMIT ? OFFSET ?
    ''', (limit, offset))
    return cursor.fetchall()

# Procedure to delete data by username or phone
def delete_data(identifier):
    cursor.execute('''
        DELETE FROM phonebook
        WHERE user_name = ? OR phone_number = ?
    ''', (identifier, identifier))
    conn.commit()

# Main function to interact with the user
def main():
    while True:
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Phonebook")
        print("4. View Phonebook")
        print("5. Save and Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            user_name = input("Enter name of the contact: ")
            phone_number = input("Enter phone number of the contact: ")
            insert_or_update_user(user_name, phone_number)
            print("Contact added successfully.")
        
        elif choice == "2":
            identifier = input("Enter name or phone number of the contact to delete: ")
            delete_data(identifier)
            print("Contact deleted successfully.")
        
        elif choice == "3":
            pattern = input("Enter search pattern: ")
            results = search_records(pattern)
            print("Search results:")
            for result in results:
                print(result[1], "-", result[2])
        
        elif choice == "4":
            print("Phonebook:")
            phonebook = query_with_pagination(limit=10, offset=0)
            for contact in phonebook:
                print(contact[1], "-", contact[2])
        
        elif choice == "5":
            conn.close()
            print("Phonebook saved and program exited.")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()