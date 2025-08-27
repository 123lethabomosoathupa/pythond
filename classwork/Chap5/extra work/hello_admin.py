# 5-10. Checking Usernames

# List of current users
current_users = ['John', 'Alice', 'Bob', 'Charlie', 'Diana']

# List of new users (some duplicates, some new)
new_users = ['BOB', 'diana', 'Eve', 'Frank', 'George']

# Create a lowercase version of current_users for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Check each new user
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different one.")
    else:
        print(f"The username '{new_user}' is available!")
