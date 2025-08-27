# ------------------------------------------
# 1. Function with required parameters in fixed order
# ------------------------------------------

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Call the function with positional arguments
describe_pet('dog', 'brock lesnar')  # I have a dog. My dog's name is Brock Lesnar.
describe_pet('dog', 'willie')        # I have a dog. My dog's name is Willie.

# Call the function with keyword arguments (order doesn't matter here)
describe_pet(animal_type='hamster', pet_name='harry')  # I have a hamster. My hamster's name is Harry.


# ------------------------------------------
# 2. Function with a default parameter value
# ------------------------------------------

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Call with only pet_name (animal_type uses default: 'dog')
describe_pet(pet_name='willie')  
# Output:
# I have a dog.
# My dog's name is Willie.

# Call with both parameters as keywords
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
# Output for both:
# I have a hamster.
# My hamster's name is Harry.

# ------------------------------------------
# 3. This will cause an ERROR
# ------------------------------------------
describe_pet()
# ❌ Error: Missing required argument 'pet_name'
# Even though animal_type has a default value, pet_name does NOT,
# so it must always be provided.
