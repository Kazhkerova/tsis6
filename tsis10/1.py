import csv

def read_phonebook_csv(path):
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            phonebook = [row for row in reader]
            return phonebook
    except FileNotFoundError:
        print("Phonebook file not found.")
        return []

def write_phonebook_csv(phonebook, path):
    try:
        with open(path, 'w', newline='') as file:
            fieldnames = ['user_name', 'phone_number']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for contact in phonebook:
                writer.writerow(contact)
        print("Phonebook updated successfully.")
    except IOError:
        print("Error writing to phonebook file.")

def add_contact(phonebook, user_name, phone_number):
    new_contact = {'user_name': user_name, 'phone_number': phone_number}
    phonebook.append(new_contact)
    print("Contact added successfully.")
    return phonebook

def delete_contact(phonebook, user_name):
    updated_phonebook = [contact for contact in phonebook if contact['user_name'] != user_name]
    if len(updated_phonebook) < len(phonebook):
        print("Contact deleted successfully.")
        return updated_phonebook
    else:
        print("Contact not found.")
        return phonebook

def view_phonebook(phonebook):
    print("\nPhonebook:")
    for contact in phonebook:
        print(contact['user_name'], "-", contact['phone_number'])

def main():
    phonebook_path = "phonebook.csv"
    phonebook = read_phonebook_csv(phonebook_path)
    
    while True:
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. View Phonebook")
        print("4. Save and Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            user_name = input("Enter name of the contact: ")
            phone_number = input("Enter phone number of the contact: ")
            phonebook = add_contact(phonebook, user_name, phone_number)
        
        elif choice == "2":
            user_name = input("Enter name of the contact to delete: ")
            phonebook = delete_contact(phonebook, user_name)
        
        elif choice == "3":
            view_phonebook(phonebook)
        
        elif choice == "4":
            write_phonebook_csv(phonebook, phonebook_path)
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()