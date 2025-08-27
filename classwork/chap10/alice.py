from pathlib import Path

# Create a Path object that points to the file location
path = Path('H:\CodeCollege\WebDev\Python\python_work\classwork\chap10\Alice.txt')

# Try to open and read the file
try:
    # Read the contents of the file using UTF-8 encoding
    contents = path.read_text(encoding='utf-8')

# If the file is not found, handle the error
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

# If the file was read successfully, process its contents
else:
    # Split the text into individual words
    words = contents.split()
    
    # Count how many words there are
    num_words = len(words)
    
    # Display the total word count to the user
    print(f"The file {path} has about {num_words} words.")
