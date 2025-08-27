# Define a dictionary called 'users' that contains information about two users.
# Each key in 'users' is a username (string), and its value is another dictionary
# containing details like first name, last name, and location.
users = {
    'aeinstein': {  # First user with username 'aeinstein'
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {  # Second user with username 'mcurie'
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

# Loop through each item (key-value pair) in the 'users' dictionary
# 'username' will store the key, and 'user_info' will store the nested dictionary of details.
for username, user_info in users.items():
    # Print the username
    print(f"\nUsername: {username}")
    
    # Combine first and last names into one string
    full_name = f"{user_info['first']} {user_info['last']}"
    
    # Get the user's location
    location = user_info['location']
    
    # Print the full name with proper capitalization
    print(f"\tFull name: {full_name.title()}")
    
    # Print the location with the first letter of each word capitalized
    print(f"\tLocation: {location.title()}")
