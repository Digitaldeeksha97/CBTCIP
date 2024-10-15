class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class ContactMaster:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"Contact '{name}' already exists.")
        else:
            self.contacts[name] = Contact(name, phone, email)
            print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts.values():
                print(contact)

    def search_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(contact)
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' not found.")


def main():
    contact_master = ContactMaster()

    while True:
        print("\nContact Master Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact_master.add_contact(name, phone, email)

        elif choice == '2':
            contact_master.view_contacts()

        elif choice == '3':
            name = input("Enter name to search: ")
            contact_master.search_contact(name)

        elif choice == '4':
            name = input("Enter name to delete: ")
            contact_master.delete_contact(name)

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
