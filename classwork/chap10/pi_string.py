from pathlib import Path

# Define the path to the file (the second assignment overwrites the first)
# First path points to pi_digits.txt, but it gets replaced by message.txt immediately
path = Path('H:\CodeCollege\WebDev\Python\python_work\classwork\chap10\pi_digits.txt')
path = Path('H:\CodeCollege\WebDev\Python\python_work\classwork\chap10\message.txt')

# Read the entire contents of the file as a single string
contents = path.read_text()

# Split the text into a list of lines (without the newline characters)
lines = contents.splitlines()

# Initialize an empty string to build the combined text
pi_string = ''

# Loop through each line in the file
for line in lines:
    pi_string += line.lstrip()  # Add the line without leading spaces
    pi_string += line           # Then add the line again in its original form

# Print the full combined string
print(f"\n{pi_string}\n")

# Print the first 52 characters of the string followed by "..."
print(f"{pi_string[:52]}...")

# Print the length of the final string
print(len(pi_string))

# Print the length again with "..." after it
print(f"{len(pi_string)}...")
