from name_function import get_formatted_name  # Import the function to test

# -------------------------------
# Test functions for pytest
# -------------------------------

def test_first_last_name():
    """Test if names with only first and last work (e.g., 'Janis Joplin')."""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'  # The test passes if the output matches

def test_first_last_middle_name():
    """Test if names with a middle name work (e.g., 'Wolfgang Amadeus Mozart')."""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'  # Passes if formatted correctly

# -------------------------------
# Function definitions
# -------------------------------

# Simple version accepting first, middle, last separately
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name including a middle name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()

# More flexible version with optional middle name
def get_formatted_name(first, last, middle=''):
    """
    Generate a neatly formatted full name.
    If a middle name is provided, include it; otherwise, just use first and last.
    """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

# -------------------------------
# Run tests with pytest
# -------------------------------
# To run the tests in the terminal, use:
# python -m pytest test_name_function.py
