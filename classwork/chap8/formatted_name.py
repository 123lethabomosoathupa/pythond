# # Define a function to return a neatly formatted full name with first and last name
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"  # Combine first and last name with a space
#     return full_name.title()  # Capitalize the first letter of each name

# # Call the function with two arguments and store the result in 'musician'
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)  # Output: Jimi Hendrix

# # Redefine the function to include a required middle name
# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {middle_name} {last_name}"  # Include middle name
#     return full_name.title()

# # Call the new version of the function with three arguments
# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)  # Output: John Lee Hooker

# # Redefine the function again — now the middle name is optional
# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:  # If a middle name is provided
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:  # If no middle name, just use first and last
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# # Call the final version with two arguments (middle name omitted)
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)  # Output: Jimi Hendrix

# # Call the final version with all three names
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)  # Output: John Lee Hooker

# # ------------------------------------------
# # First infinite loop version (no quit condition)
# # ------------------------------------------

# # Define a basic two-name formatting function again
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# # This is an infinite loop (no way to exit unless forced)
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")  # Get first name from user
#     l_name = input("Last name: ")   # Get last name from user
#     formatted_name = get_formatted_name(f_name, l_name)  # Format full name
#     print(f"\nHello, {formatted_name}!")  # Greet the user

# ------------------------------------------
# Improved loop version (with 'q' to quit)
# ------------------------------------------

# Define the same formatting function again
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Loop until the user enters 'q' to quit
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':  # Quit if user enters 'q'
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':  # Quit if user enters 'q'
        break
    
    formatted_name = get_formatted_name(f_name, l_name)  # Format full name
    print(f"\nHello, {formatted_name}!")  # Greet the user
