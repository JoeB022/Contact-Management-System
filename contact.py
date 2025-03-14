import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from the file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to the file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter the contact's name: ").strip()
    phone = input("Enter the contact's phone number: ").strip()
    email = input("Enter the contact's email address: ").strip()

    if name in contacts:
        print("A contact with this name already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print(f"Contact '{name}' added successfully.")

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def edit_contact(contacts):
    """Edit an existing contact."""
    name = input("Enter the name of the contact you want to edit: ").strip()
    if name in contacts:
        print(f"Editing contact: {name}")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
        email = input(f"Enter new email address (current: {contacts[name]['email']}): ").strip()

        contacts[name]["phone"] = phone if phone else contacts[name]["phone"]
        contacts[name]["email"] = email if email else contacts[name]["email"]
        save_contacts(contacts)
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact you want to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    """Main function to run the contact management program."""
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()