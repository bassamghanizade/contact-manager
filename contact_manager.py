import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        if not name or not phone or not email:
            print("All fields are required.")
            return

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Name alredy exists.")
                return
            if contact.phone == phone:
                print("Phone already exists.")
                return
            if contact.email.lower() == email.lower():
                print("Email already exists.")
                return

        self.contacts.append(Contact(name, phone, email))
        print("Contact added successfully.")

    def show_contacts(self):
            if not self.contacts:
                print("No contacts to show.")
                return

            for i, contact in enumerate(self.contacts, start=1):
                print("-" * 20)
                print(f"{i}. Name :{contact.name}")
                print(f"   Phone :{contact.phone}")
                print(f"   Email :{contact.email}")
                print("-" * 20)
        
    def search_contact(self, name):
            for contact in self.contacts:
                if contact.name.lower() == name.lower():
                    print("-" * 20)
                    print(f"Name :{contact.name}")
                    print(f"Phone :{contact.phone}")
                    print(f"email :{contact.email}")
                    print("-" * 20)
                    return
           
            print("Contact not found.")

    def delete_contact(self):
        if not self.contacts:
            print("No contacts to delete.")
            return

        self.show_contacts()
        try:
            index = int(input("Enter contact number to delete: "))
        except ValueError:
            print("Please enter a valid number.")
            return
 
        if index < 1 or index > len(self.contacts):
            print("Number out of range.")
            return

        contact = self.contacts[index - 1]
        confirm = input(f"Delete contact {contact.name}?(yes/no): ").lower()

        if confirm == "yes":
            self.contacts.pop(index - 1)
            print("Contact deleted successfully.")
        else:
            print("Delete cancelled.")

    def edit_contact(self):
        if not self.contacts:
            print("No contact to edit.")
            return

        self.show_contacts()
        try:
            index = int(input("Enter contact number to edit: "))
        except ValueError:
            print("Invalid number.")
            return

        if index < 1 or index > len(self.contacts):
            print("Number put is out of range.")
            return

        contact = self.contacts[index - 1]

        print("Leave blank to keep current value.")
        new_name = input(f"New name({contact.name}): ").strip()
        new_phone = input(f"New phone({contact.phone}): ").strip()
        new_email = input(f"New email({contact.email}): ").strip()

        if new_name:
            contact.name = new_name
        if new_phone:
            contact.phone = new_phone
        if new_email:
            contact.email = new_email

        print("Contact updated successfully.")

    def save_to_file(self, filename="contacts.json"):
        data = [{"name": c.name, "phone": c.phone, "email": c.email} for c in self.contacts]
        with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        
    def load_from_file(self, filename="contacts.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    self.contacts = []
                    return

                data = json.loads(content)
                self.contacts = [Contact(d["name"], d["phone"], d["email"]) for d in data]

        except FileNotFoundError:
            self.contacts = []

        except FileNotFoundError:
            print("contacts.json is corrupted. Staring with empty list.") 
            self.contacts = []
     


def main():
    manager = ContactManager()
    manager.load_from_file()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add contact")
        print("2. Show contacts")
        print("3. Search contact")
        print("4. Edit contact")
        print("5. Delete contact")
        print("6. Save and Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            manager.add_contact(
                input("Name: "),
                input("Phone: "),
                input("Email: "),)
         
        elif choice == "2":
            manager.show_contacts()
 
        elif choice == "3":                
            manager.search_contact(input("Enter name to search: "))

        elif choice == "4":
            manager.edit_contact()

        elif choice == "5":
            manager.delete_contact()

        elif choice == "6":
            manager.save_to_file()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

    
if __name__ == "__main__":
    main()
