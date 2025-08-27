# List of usernames including 'admin'
usernames = ['alice', 'admin', 'jaden', 'maria', 'leo']

# Loop through each user in the list
for username in usernames:
    # Check if the user is 'admin'
    if username == 'admin':
        # Special greeting for admin
        print("Hello admin, would you like to see a status report?")
    else:
        # Generic greeting for other users
        print(f"Hello {username.title()}, thank you for logging in again.")
