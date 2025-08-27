def get_formatted_name(first, last):
    """
    Generate a neatly formatted full name.
    
    Parameters:
    first (str): The person's first name.
    last (str): The person's last name.

    Returns:
    str: The full name with each word capitalized.
    """
    # Combine first and last name into one string
    full_name = f"{first} {last}"
    
    # Convert the name to title case (capitalize each word)
    return full_name.title()
