from pathlib import Path
import json

# Create a Python list of numbers
numbers = [2, 3, 5, 7, 11, 13]

# Create a Path object for the file 'Numbers.json'
path = Path('Numbers.json')

# Convert the Python list into a JSON-formatted string
contents = json.dumps(numbers)

# Write the JSON string to the file (creates the file if it doesn't exist)
path.write_text(contents)
