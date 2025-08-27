print("\n\tPart 1")
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    # *toppings collects all positional arguments into a tuple called toppings
    print("\nMaking a pizza with the following toppings:")
    print(toppings)  # Print the raw tuple of toppings

# Call make_pizza with a single topping
make_pizza('pepperoni')

# Call make_pizza with multiple toppings
make_pizza('mushrooms', 'green peppers', 'extra cheese')


print("\n\tPart 2")
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    # Loop through the toppings tuple and print each topping on its own line
    for topping in toppings:
        print(f"- {topping}")

# Call make_pizza with a single topping
make_pizza('pepperoni')

# Call make_pizza with multiple toppings
make_pizza('mushrooms', 'green peppers', 'extra cheese')


print("\n\tPart 3")
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    # The first argument 'size' is a required positional argument for pizza size
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    # Loop through toppings and print each topping on its own line
    for topping in toppings:
        print(f"- {topping}")

# Call make_pizza specifying the pizza size and toppings
make_pizza(16, 'pepperoni')

# Call make_pizza specifying a smaller size and multiple toppings
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


#part 4
print("\n\tPart 4")
def make_pizza(size, *toppings):
 """Summarize the pizza we are about to make."""
 print(f"\nMaking a {size}-inch pizza with the following toppings:")
 for topping in toppings:
  print(f"- {topping}")