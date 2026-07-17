import json
from validators import (
    validate_name,
    validate_phone,
    validate_email,
)


def show_contact(data=None):

    """
    Display contacts in a formatted contact list.

    If no data is provided, the function loads all contacts from the
    JSON file. Otherwise, it displays the given contact data using
    the predefined format.

    Args:
        data: A dictionary containing contact information to display.
            If None, all contacts are loaded from the JSON file.

    Returns:
        None.
    """

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

    """
    Add a new contact to the contact list.

    The provided name, phone number, and email address are validated
    before the contact is added. If all values are valid, the contact
    is saved to the JSON file.

    Args:
        name: The contact's name.
        phone: The contact's phone number.
        email: The contact's email address.

    Returns:
        True if the contact is added successfully, otherwise False.
    """

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

    """
    Delete a contact from the contact list.

    The contact is identified by its contact ID. If the contact exists,
    it is removed from the contact list and the remaining contacts are
    renumbered before the updated data is saved to the JSON file.

    Args:
        contact_id: The ID of the contact to delete.

    Returns:
        True if the contact is deleted successfully, otherwise False.
    """

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

    """
    Edit a contact's information.

    The contact is identified by its contact ID. Depending on the selected
    mode, the function updates the contact's name, phone number, or email
    address. The new value is validated before being saved to the JSON file.

    Args:
        contact_id: The ID of the contact to edit.
        mode: The field to update. Must be one of "name", "phone", or
            "email".

    Returns:
        True if the contact is updated successfully, otherwise False.
    """

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

    """
    Search for contacts using a keyword.

    Depending on the selected mode, the function searches by name, phone
    number, email address, or all fields. All matching contacts are
    displayed in a formatted contact list.

    Args:
        keyword: The keyword used to search for contacts.
        mode: The search mode. Must be one of "all", "name", "phone",
            or "email". Defaults to "all".

    Returns:
        True if the search is completed successfully, otherwise False.
    """

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

    """
    Delete all contacts from the contact list after confirmation.

    If the user confirms the operation by entering "Y" or "y", all
    contacts are removed from the JSON file. If the user enters "N"
    or "n", the operation is cancelled.

    Args:
        confirmation: The user's confirmation. Must be "Y", "y", "N",
            or "n".

    Returns:
        True if the operation is processed successfully, otherwise False.
    """

    if not isinstance(confirmation, str):
        print("Invalid input!")
        return False

    confirmation = confirmation.strip().lower()

    if confirmation not in ("y", "n"):
        print("Please enter Y or N!")
        return False

    if confirmation == "y":
        with open("data.json", "w", encoding="UTF-8") as file:
            json.dump({}, file, ensure_ascii=False, indent=4)
        print("All contacts have been deleted!")
    else:
        print("Operation cancelled.")

    return True