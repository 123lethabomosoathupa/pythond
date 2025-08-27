# Define the initial prompt message asking the user for the name of a city they've visited
prompt = "\nPlease enter the name of a city you have visited:"
# Add instructions for quitting the loop when finished
prompt += "\n(Enter 'quit' when you are finished.) "

# Start an infinite loop to continuously ask for user input
while True:
    # Get the city name from the user
    city = input(prompt)
    
    # Check if the user wants to quit the loop
    if city == 'quit':
        break  # Exit the loop if the user types 'quit'
    else:
        # Print a message showing interest in the city the user entered
        print(f"I'd love to go to {city.title()}!")

