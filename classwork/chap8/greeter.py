# # Define a function that displays a simple greeting without needing any input
# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")  # Print a basic greeting message

# # Call the first version of the function
# greet_user()

# ------------------------------------------
# Redefine the function to accept a parameter (username)
# ------------------------------------------

def greet_user(username):
    """Display a personalized greeting."""
    # Use f-string to insert the username and format it with the first letter capitalized
    print(f"Hello, {username.title()}!")

# Call the second version of the function with the name 'lethabo'
greet_user('lethabo')  # Output: Hello, Lethabo!
