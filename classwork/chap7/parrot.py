# Ask the user for a message and print it back
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Create a prompt message that includes instructions for quitting
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# Initialize message to an empty string
message = ""

# Loop until the user types 'quit'
# while message != 'quit':
#     message = input(prompt)
#     print(message)  # This will still print 'quit' before ending

# A better version: use a flag to control the loop and avoid printing 'quit'
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False  # End the loop
    else:
        print(message)  # Only print if the message isn't 'quit'
