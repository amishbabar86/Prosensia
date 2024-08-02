# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the contact name: ").strip().title()
    phone_number = input("Enter the contact phone number: ").strip()

    # Check if the contact already exists
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print(f"Contact '{name}' already exists!")
            return

    # Add the contact if it doesn't exist
    contacts.append((name, phone_number))
    print(f"Contact '{name}' added successfully!")

# Function to search for a contact by name
def search_contact(contacts):
    search_name = input("Enter the name to search: ").strip().title()
    found = False

    for contact in contacts:
        if contact[0].lower() == search_name.lower():
            print(f"Found contact: {contact[0]} - {contact[1]}")
            found = True
            break
    
    if not found:
        print(f"Contact '{search_name}' not found.")

# Function to display all contacts
def display_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
    else:
        print("All Contacts:")
        for contact in contacts:
            print(f"{contact[0]} - {contact[1]}")

# Main function to manage the flow of the program
def main():
    contacts = []
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            display_contacts(contacts)
        elif choice == '4':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
