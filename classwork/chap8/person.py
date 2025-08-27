# ------------------------------------------
# 1. Simple function to build a dictionary representing a person
# ------------------------------------------

# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person."""
#     # Create a dictionary with keys 'first' and 'last'
#     person = {'first': first_name, 'last': last_name}
#     return person  # Return the dictionary to the caller

# # Call the function with first and last name
# musician = build_person('jimi', 'hendrix')

# # Print the dictionary that was returned
# print(musician)  # Output: {'first': 'jimi', 'last': 'hendrix'}


# # ------------------------------------------
# # 2. Function to return a neatly formatted full name (middle name optional)
# # ------------------------------------------

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         # If a middle name was provided, include it
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         # Otherwise, just use first and last
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()  # Capitalize each word in the name

# # Call the function without a middle name
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)  # Output: Jimi Hendrix

# # Call the function with a middle name
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)  # Output: John Lee Hooker


# # ------------------------------------------
# # 3. Enhanced build_person function that can also store age
# # ------------------------------------------

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    # Basic dictionary with first and last name
    person = {'first': first_name, 'last': last_name}
    
    # If age is provided (not None), add it to the dictionary
    if age:
        person['age'] = age
    return person  # Return the dictionary

# Call the enhanced function with age included
musician = build_person('jimi', 'hendrix', age=27)
print(musician)  # Output: {'first': 'jimi', 'last': 'hendrix', 'age': 27}
