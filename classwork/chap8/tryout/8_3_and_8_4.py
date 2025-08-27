print("\n\tExercise 8.3\n")

# Define the function
def make_shirt(size, message):
    print(f"The shirt size is {size} and it will say: '{message}'.")

# Call the function using positional arguments
make_shirt("Medium", "I'm Rick James")

# Call the function using keyword arguments
make_shirt(size="Large", message="Suplex City")


print("\n\tExercise 8.4\n")

# Define the function with default values
def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and it will say: '{message}'.")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt(size="Medium")

# Any size with a different message
make_shirt(size="Small", message="Code all day!")
