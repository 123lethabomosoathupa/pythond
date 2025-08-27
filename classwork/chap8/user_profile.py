# ------------------------------------------
# Function to build a user profile
# ------------------------------------------
def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything we know about a user.
    - first: user's first name (required)
    - last: user's last name (required)
    - **user_info: any number of additional key-value pairs
    """
    # Add first and last name to the dictionary
    user_info['first_name'] = first
    user_info['last_name'] = last
    
    return user_info  # Return the completed dictionary


# ------------------------------------------
# Create a profile for Albert Einstein
# ------------------------------------------
user_profile = build_profile(
    'albert', 'einstein',   # Positional arguments for first & last name
    location='princeton',   # Additional info (keyword arguments)
    field='physics'         # Additional info
)

# Print the profile dictionary
print(user_profile)
# Example Output:
# {'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
