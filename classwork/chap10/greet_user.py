from pathlib import Path
import json

# Create a Path object pointing to the file 'username.json'
path = Path('username.json')

# Read the entire content of the file as a string
contents = path.read_text()

# Convert the JSON string into a Python object (e.g., a string, list, or dict)
username = json.loads(contents)

# Greet the user using the loaded username
print(f"Welcome back, {username}! You need a Cuban Cigar!!!")
