import json
def validate_name(name: str) -> bool:
    if not name.strip():
        print("Name cannot be empty!")
        return False

    if len(name) > 50:
        print("Name is too long!")
        return False

    return True

def validate_phone(phone: str) -> bool:
    if not phone.isdigit():
        print("Phone number must contain digits only!")
        return False
    if not 9 <= len(phone) <= 15:
        print("Phone number must be between 9 and 15 digits!")
        return False
    
    return True

def validate_email(email: str) -> bool:
    if len(email) > 254:
        print("Email is too long!")
        return False
    if "@" not in email:
        print("Email must contain '@'!")
        return False
    
    return True

def show_contact(data=None):
    if data is None:
        with open("data.json", "r", encoding="UTF-8") as file:
            data = json.load(file)
    
    if not data:
        print("Contact list is empty!")
        return False

    print(
        "=============== CONTACT LIST ===============\n\n",
        "\n".join(
            f"[{contact_id}]\n"
            f"Name: {contact_info['name']}\n"
            f"Phone: {contact_info['phone']}\n"
            f"Email: {contact_info['email']}\n"
            for contact_id, contact_info in data.items()
        ),
        "\n=============== CONTACT LIST ===============\n",
        sep=""
    )


def add_contact(name: str, phone: str, email: str) -> bool:
    if (not validate_name(name) or not validate_email(email) or not validate_phone(phone)):
        return False

    with open("data.json", "r", encoding="UTF-8") as file:
        data = json.load(file)

        data[str(len(data) + 1)] = {
            "name": name,
            "phone": phone,
            "email": email
        }

    with open("data.json", "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("Contact added successfully!")
    return True

def delete_contact(contact_id: str) -> bool:
    with open("data.json", "r", encoding="UTF-8") as file:
        old_data = json.load(file)
        new_data = {}

        if not contact_id.isdigit():
            print("Please enter a valid contact ID!")
            return False

        if contact_id not in old_data:
            print("Contact ID does not exist!")
            return False

        old_data.pop(contact_id)

        for new_id, old_id in enumerate(old_data, start=1):
            new_data[str(new_id)] = old_data[old_id]

    with open("data.json", "w", encoding="UTF-8") as file:
        json.dump(new_data, file, indent=4, ensure_ascii=False)

    print("Contact deleted successfully!")
    return True


def edit_contact(contact_id: str, mode="name") -> bool:
    validators = {
    "name": validate_name,
    "phone": validate_phone,
    "email": validate_email
    }

    prompts = {
        "name": "Enter new name: ",
        "phone": "Enter new phone number: ",
        "email": "Enter new email: "
    }
    mode = mode.lower()

    if mode not in ("name", "phone", "email"):
        print("Invalid mode!")
        return False

    with open("data.json", "r", encoding="UTF-8") as file:
        data = json.load(file)

        if not contact_id.isdigit():
            print("Please enter a valid contact ID!")
            return False

        if contact_id not in data:
            print("Contact ID does not exist!")
            return False

        while True:
            new_value = input(prompts[mode])

            if not validators[mode](new_value):
                continue

            break

        data[contact_id][mode] = new_value

    with open("data.json", "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("Contact updated successfully!")
    return True

def search_contact(keyword: str, mode="all") -> bool:
    if not isinstance(keyword, str):
        print("Invalid keyword!")
        return False

    if not isinstance(mode, str) or mode not in ("name", "phone", "email", "all"):
        print("Invalid mode!")
        return False

    keyword = keyword.lower()
    mode = mode.lower()

    if not keyword.strip():
        print("Keyword cannot be empty!")
        return False

    with open("data.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
        matched_contacts = {}

        for contact_id, contact in data.items():
            if mode == "all":
                if any(keyword in str(value).lower() for value in contact.values()):
                    matched_contacts[contact_id] = contact
            else:
                if keyword in str(contact[mode]).lower():
                    matched_contacts[contact_id] = contact

    show_contact(data=matched_contacts)

    return True


def clear_contact(confirmation: str) -> bool:
    if not isinstance(confirmation, str):
        print("Invalid input!")
        return False

    confirmation = confirmation.strip().lower()

    if confirmation == "y":
        with open("data.json", "w", encoding="UTF-8") as file:
            json.dump({}, file, ensure_ascii=False, indent=4)
        print("All contacts have been deleted!")
    else:
        print("Operation cancelled.")

    return True


while True:
    print("""
    ========== CONTACT MANAGER ==========

    1. View Contacts
    2. Add Contact
    3. Delete Contact
    4. Edit Contact
    5. Search Contacts
    6. Clear All Contacts
    7. Exit

    ====================================
    """)

    choice = input("Enter your choice (1-7): ")

    if not choice.isdigit():
        print("Invalid input!")
        continue

    if not 1 <= int(choice) <= 7:
        print("Please enter a number between 1 and 7.")
        continue

    if choice == "1":
        show_contact()
        input("Press Enter to continue...")

    elif choice == "2":
        while True:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")

            if add_contact(name, phone, email):
                break

    elif choice == "3":
        while True:
            contact_id = input("Enter contact ID to delete: ")

            if delete_contact(contact_id):
                break

    elif choice == "4":
        while True:
            contact_id = input("Enter contact ID: ")
            mode = input("Enter field to edit (name/phone/email): ")

            if edit_contact(contact_id, mode):
                break

    elif choice == "5":
        while True:
            mode = input("Enter search mode (name/phone/email/all): ")
            keyword = input("Enter keyword: ")

            if search_contact(keyword, mode):
                input("Press Enter to continue...")
                break

    elif choice == "6":
        while True:
            confirmation = input("Are you sure you want to delete all contacts? (Y/N): ")

            if clear_contact(confirmation):
                break

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Unexpected error occurred.")
else:
    print("Unexpected error occurred.")