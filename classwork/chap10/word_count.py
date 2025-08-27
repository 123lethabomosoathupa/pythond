from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        # Try to read the file as text using UTF-8 encoding
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # If the file is not found, ignore the error
        # (You could uncomment the print statement to show a warning)
      #   pass
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file
        words = contents.split()   # Split text into a list of words
        num_words = len(words)     # Count the number of words
        print(f"\nThe file {path} has about {num_words} words.\n")

# Path to the first file to check
path = Path('H:\CodeCollege\WebDev\Python\python_work\classwork\chap10\Alice.txt')
count_words(path)  # Call the function for the first file

# List of file paths to check word counts for
filenames = [
    'H:\CodeCollege\WebDev\Python\python_work\classwork\chap10\Alice.txt',
    'H:\CodeCollege\WebDev\Python\python_work\classwork\chap10\siddhartha.txt',
    'H:\CodeCollege\WebDev\Python\python_work\classwork\chap10\moby_dick.txt',
    'H:\CodeCollege\WebDev\Python\python_work\classwork\chap10\little_women.txt'
]

# Loop through each filename, create a Path object, and count words
for filename in filenames:
    path = Path(filename)
    count_words(path)
