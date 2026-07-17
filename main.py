from contacts import (
    show_contact,
    add_contact,
    delete_contact,
    edit_contact,
    search_contact,
    clear_contact,
)


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