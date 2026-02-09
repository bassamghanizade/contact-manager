FILE_NAME = "contacts.txt"

def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    if not name or not phone or not email:
        print("All field are required.")
        return

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Name already exists.")
            return
        elif contact["phone"] == phone:
            print("Phone already exists.")
            return
        elif contact["email"].lower() == email.strip():
            print("Email already exists.")
            return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("Contact added successfully.")

def show_contacts(contacts):
    if not contacts:
        print("No contacts to show.")
        return

    sorted_contacts = sorted(contacts, key=lambda c: c["name"].lower())

    for i, contact in enumerate(sorted_contacts, start=1):
        print("-" * 20)
        print(f"{i}.Name : {contact['name']}")
        print(f"(:Phone : {contact['phone']}")
        print(f"(:email : {contact['email']}")
        print("-" * 20)


def search_contact(contacts):
    name = input("Search name: ")
  
    for contact in contacts:
        if contact["name"] == name:
            print(f"{contact['name']} - {contact['phone']} - {contact['email']}")
            return

    print("contact not found.")

def delete_contact(contacts):
    show_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter contact number to delete: "))
        if index < 1 or index > len(contacts):
            print("Invalid number.")
            return
    except ValueError:
        print("Please enter a number.")
        return

    contact = contacts[index - 1]
    confirm = input(f"Are you sure you want to delete {contact['name']}? (y/n): ").lower()

    if confirm == "y":
        contacts.pop(index - 1)
        save_contacts(contacts)
        print("Contact deleted successfully.")


def edit_contact(contacts):
    show_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter contact number to edit: "))
        if index < 1 or index > len(contacts):
            print("Invalid number.")
            return
    except ValueError:
        print("please enter a number.")
        return

    contact = contacts[index - 1]

    new_name = input(f"New name({contact['name']}): ").strip()
    new_phone = input(f"New phone({contact['phone']}): ").strip()
    new_email = input(f"New email({contact['email']}): ").strip()
    
    if new_name:
        contact["name"] = new_name        
    if new_phone:
        contact["phone"] = new_phone
    if new_email:
        contact["email"] = new_email

    save_contacts(contacts)
    print("Contact updated.")


def save_contacts(contacts):
    with open(FILE_NAME, "w",encoding="utf-8") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

def load_contacts():
    contacts = []
    try:
        with open(FILE_NAME,"r", encoding="utf-8") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts.append({"name": name,
                                 "phone": phone,
                                 "email": email})
    except FileNoteFoundError:
        pass                                           
    return contacts


def main_menu():
    contact = load_contacts()
    
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
            add_contact(contact)
        elif choice == "2":
            show_contacts(contact)
        elif choice == "3":
            search_contact(contact)
        elif choice == "4":
            edit_contact(contact)
        elif choice == "5":
            delete_contact(contact)
        elif choice == "6":
            save_contacts(contact)
            print("Goodbye.")
            break
        else:
            print("invalid choice")

main_menu()
