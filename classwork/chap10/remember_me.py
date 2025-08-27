from pathlib import Path
import json

# Ask the user for their name (first prompt)
username = input("What is your name? ")

# Create a Path object for the JSON file that will store the username
path = Path('username.json')

# Check if the file exists
if path.exists():
    # If it exists, read its contents and load the username from JSON
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}! You need a Cuban Cigar!!!")
else:
    # If it does not exist, ask for the name and store it
    username = input("What is your name? ")
    contents = json.dumps(username)  # Convert Python string to JSON
    path.write_text(contents)        # Save to file
    print(f"We'll remember you when you come back, {username}!")

# This part writes the username again (even after the first check)
contents = json.dumps(username)
path.write_text(contents)
print(f"We'll remember you when you come back, {username}!")

# --- First greet_user function ---
def greet_user():
    """"Greet The User"""
    path = Path('username.json')
    if path.exists():
        # If the file exists, greet the returning user
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}! You need a Cuban Cigar!!!")
    else:
        # If not found, store a new username
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

# Call the first version of greet_user
greet_user()

# --- Helper function to load a stored username ---
def get_stored_username(path):
    """Return the stored username if the file exists, otherwise None."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

# --- Second version of greet_user that uses get_stored_username ---
def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

# Call the second version of greet_user
greet_user()
