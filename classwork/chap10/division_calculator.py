print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

# Start an infinite loop for repeated user input
while True:
    # Prompt the user for the first number
    first_number = input("\nFirst number: ")
    if first_number == 'q':  # If the user types 'q', exit the loop
        break
    
    # Prompt the user for the second number
    second_number = input("Second number: ")
    if second_number == 'q':  # If the user types 'q', exit the loop
        break

    try:
        # Convert both inputs to integers and perform the division
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        # This block runs only if the user attempts to divide by zero
        print("You can't divide by 0!")
    else:
        # If no exception occurred, display the division result
        print(answer)

# --- Example of error handling outside the loop ---
try:
    # This will trigger a ZeroDivisionError immediately
    print(5 / 0)
except ZeroDivisionError:
    # Handle the error gracefully instead of crashing
    print("You can't divide by zero!")
