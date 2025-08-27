# Create a glossary dictionary
glossary = {
    "variable": "A name that refers to a value stored in memory.",
    "function": "A block of reusable code that performs a specific task.",
    "loop": "A structure that repeats a block of code multiple times.",
    "dictionary": "A collection of key-value pairs in Python.",
    "list": "An ordered collection of items that can be changed."
}

# Print each word and its meaning neatly formatted
for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")

# Create a glossary dictionary with 10 programming terms
glossary = {
    "variable": "A name that refers to a value stored in memory.",
    "function": "A block of reusable code that performs a specific task.",
    "loop": "A structure that repeats a block of code multiple times.",
    "dictionary": "A collection of key-value pairs in Python.",
    "list": "An ordered collection of items that can be changed.",
    "tuple": "An ordered collection of items that cannot be changed (immutable).",
    "string": "A sequence of characters enclosed in quotes.",
    "boolean": "A data type that can have one of two values: True or False.",
    "if_statement": "A conditional statement that executes code based on a condition.",
    "module": "A file containing Python code that can be imported into a program."
}

# Loop through the dictionary and print each word with its meaning
for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")
