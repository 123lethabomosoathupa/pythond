# Import the Path class from the pathlib module for file path operations
from pathlib import Path

# Create the contents of the file as a string, using += to append each new line
contents = "Jackie Chan was here\n"                # First line
contents += "He loves to kick enemies\n"           # Second line
contents += "He is the original stuntman actor\n"  # Third line

# Define the file path where the text will be saved
# Note: Use raw string (r'...') or double backslashes for Windows paths
path = Path('H:\CodeCollege\WebDev\Python\python_work\classwork\chap10\programming.txt')

# Write the string contents to the file, overwriting if it already exists
path.write_text(contents)
