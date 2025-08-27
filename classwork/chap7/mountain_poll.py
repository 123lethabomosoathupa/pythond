# Create an empty dictionary to store poll responses
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

# Start a loop to collect responses while polling is active
while polling_active:
    # Ask the user for their name
    name = input("\nWhat is your name? ")

    # Ask the user which mountain they would like to climb
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary using the person's name as the key
    responses[name] = response

    # Ask if another person would like to respond
    repeat = input("Would you like to let another person respond? (yes/ no) ")

    # If the answer is 'no', stop the polling
    if repeat == 'no':
        polling_active = False

# Polling is complete, so display the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
