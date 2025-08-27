from pathlib import Path
import json

# Create a Path object pointing to the file 'Numbers.json'
path = Path('Numbers.json')

# Read the entire contents of the file as a single string
contents = path.read_text()

# Convert the JSON string into a Python object (e.g., list, dictionary, etc.)
numbers = json.loads(contents)

# Print the Python object
print(numbers)
