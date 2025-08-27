# ------------------------------------------
# 1. Importing the whole module and calling functions with module name
# ------------------------------------------
import pizza  # Import the pizza module

# Call make_pizza function from pizza module using dot notation
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# ------------------------------------------
# 2. Importing a specific function directly
# ------------------------------------------
from pizza import make_pizza  # Only import the make_pizza function

# Now we can call make_pizza() without typing pizza.
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# ------------------------------------------
# 3. Importing with an alias for the module
# ------------------------------------------
import pizza as p  # Give the module a shorter name 'p'

# Call make_pizza() through the alias
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# ------------------------------------------
# 4. Importing a function with an alias
# ------------------------------------------
from pizza import make_pizza as mp  # Give the function a shorter name 'mp'

# Call the aliased function
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# ------------------------------------------
# 5. Importing all functions and variables from a module
# ------------------------------------------
from pizza import *  # Import EVERYTHING from pizza module

# Now we can call make_pizza() directly
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
