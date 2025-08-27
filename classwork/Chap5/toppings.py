print("------PART 1-------")

# List of toppings requested by the customer
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# 

# Loop through each requested topping
for requested_topping in requested_toppings:
    # Check if the topping is 'green peppers'
    if requested_topping == 'green peppers':
        # Inform the customer that green peppers are unavailable
        print("Sorry, we are out of green peppers right now.")
    else:
        # Confirm the addition of the available topping
        print(f"Adding {requested_topping}.")

# Print a message once all toppings have been processed
print("\nFinished making your pizza!")

# List of toppings currently available in the kitchen
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

print("------PART 2-----")
# List of requested toppings (currently empty)
requested_toppings = []

# Check if the list is not empty
if requested_toppings:
    # Loop through each topping and add it to the pizza
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    # Confirm that the pizza is finished
    print("\nFinished making your pizza!")
else:
    # If the list is empty, ask the user if they want a plain pizza
    print("Are you sure you want a plain pizza?")


print("------------Part 3------------")
# List of toppings requested by the customer
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# Loop through each requested topping to check availability
for requested_topping in requested_toppings:
    # If the topping is available, confirm adding it
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        # If not available, inform the customer
        print(f"Sorry, we don't have {requested_topping}.")

# Message after processing all requested toppings
print("\nFinished making your pizza!")

