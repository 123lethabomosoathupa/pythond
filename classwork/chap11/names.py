from name_function import get_formatted_name

# Let the user know they can quit at any time
print("Enter 'q' at any time to quit.")

# Start an infinite loop to get user input repeatedly
while True:
    # Ask the user for their first name
    first = input("\nPlease give me a first name: ")
    if first == 'q':  # Exit the loop if the user types 'q'
        break

    # Ask the user for their last name
    last = input("Please give me a last name: ")
    if last == 'q':  # Exit the loop if the user types 'q'
        break

    # Call the get_formatted_name() function to format the name
    formatted_name = get_formatted_name(first, last)

    # Display the neatly formatted full name
    print(f"\n\tNeatly formatted name: {formatted_name}.")
