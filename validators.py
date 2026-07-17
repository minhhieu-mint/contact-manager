def validate_name(name: str) -> bool:

    """
    Validate a contact name.

    The name must not be empty and must not exceed 50 characters.

    Args:
        name: The contact name to validate.

    Returns:
        True if the name is valid, otherwise False.
    """

    if not name.strip():
        print("Name cannot be empty!")
        return False

    if len(name) > 50:
        print("Name is too long!")
        return False

    return True

def validate_phone(phone: str) -> bool:

    """
    Validate a phone number.

    A valid phone number must contain digits only and have a length
    between 9 and 15 characters.

    Args:
        phone: The phone number to validate.

    Returns:
        True if the phone number is valid, otherwise False.
    """

    if not phone.isdigit():
        print("Phone number must contain digits only!")
        return False
    if not 9 <= len(phone) <= 15:
        print("Phone number must be between 9 and 15 digits!")
        return False
    
    return True

def validate_email(email: str) -> bool:

    """
    Validate an email address.

    A valid email address must contain at least one '@' character
    and must not exceed 254 characters.

    Args:
        email: The email address to validate.

    Returns:
        True if the email address is valid, otherwise False.
    """

    if len(email) > 254:
        print("Email is too long!")
        return False
    if "@" not in email:
        print("Email must contain '@'!")
        return False
    
    return True