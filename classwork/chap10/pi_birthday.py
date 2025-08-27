from pathlib import Path

# Create a Path object that points to the file containing digits of pi
# Note: Use double backslashes (\\) or a raw string (r"...") to avoid escape sequence errors
path = Path('H:\\CodeCollege\\WebDev\\Python\\python_work\\classwork\\chap10\\pi_digits.txt')

# Read the entire contents of the file into a single string
contents = path.read_text()

# Print the file exactly as it is
print(contents)

# Split the file contents into a list of lines
lines = contents.splitlines()

# Create an empty string to store all digits of pi as one continuous number
pi_string = ''

# Loop through each line in the file
for line in lines:
    # Remove any whitespace from the start/end of the line and append to pi_string
    pi_string += line.strip()

# Ask the user for their birthday in the format mmddyy
birthday = input("Enter your birthday, in the form mmddyy: ")

# Check if the entered birthday sequence appears anywhere in pi_string
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
