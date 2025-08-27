# Ask the user to enter their name and store it in the variable 'name'
name = input("Please enter your name: ")

# Greet the user using their input
print(f"\nHello, {name}!")

# Create a prompt message split across two lines for readability
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

# Ask for the user's first name using the prompt message
name = input(prompt)

# Greet the user again with the personalized message
print(f"\nHello, {name}!")
