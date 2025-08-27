# Define a function that greets each user in a provided list
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:  # Loop through each name in the list
        msg = f"Hello, {name.title()}!"  # Capitalize the first letter of the name
        print(msg)  # Display the greeting message

# Create a list of usernames
usernames = ['hannah', 'ty', 'margot']

# Call the function with the list of usernames
greet_users(usernames)
