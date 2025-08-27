# ------------------------------------------
# Function to simulate the printing process
# ------------------------------------------
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left.
    Move each design to completed_models after printing.
    """
    print("\nThe following models are to be printed:")
    
    # While there are still designs left to print
    while unprinted_designs:
        # Remove the last design from the unprinted list
        current_design = unprinted_designs.pop()
        
        # Simulate the printing process
        print(f"Printing model: {current_design}")
        
        # Add the design to the list of completed models
        completed_models.append(current_design)


# ------------------------------------------
# Function to display all completed models
# ------------------------------------------
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    
    # Loop through the list and print each completed model
    for completed_model in completed_models:
        print(completed_model)


# ------------------------------------------
# Main program
# ------------------------------------------
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']  # Initial designs
completed_models = []  # Start with an empty completed list

# Call function to simulate printing
print_models(unprinted_designs, completed_models)

# Call function to display completed models
# NOTE: Here you passed completed_models[:] which is a COPY of the list
#       so the original list remains unchanged if the function modifies it.
show_completed_models(completed_models[:])
