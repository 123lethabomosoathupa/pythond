from pathlib import Path

# Create a Path object that points to the file location
# Note: Use double backslashes (\\) or raw strings (r'...') to avoid escape sequence issues
path = Path('H:\\CodeCollege\\WebDev\\Python\\python_work\\classwork\\chap10\\pi_digits.txt')

# Read the entire contents of the file into a single string
contents = path.read_text()

# Print the whole file contents as they are
print(contents)

# Split the file contents into a list of lines (removing the newline characters)
lines = contents.splitlines()

# Loop through each line in the list and print it
for line in lines:
    print(line)
