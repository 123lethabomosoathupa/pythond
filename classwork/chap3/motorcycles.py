# Create a list of motorcycle brands
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# Add a new motorcycle brand to the end of the list
# motorcycles.append('ducati')
# print(motorcycles)

# Change the first item in the list to 'ducati'
# motorcycles[0] = 'ducati'
# print(motorcycles)

# Start with an empty list and add items one by one
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

# Insert 'ducati' at the beginning of the list
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducati')
# print(motorcycles)

# Delete the first item in the list
# del motorcycles[0]
# print(motorcycles)

# Delete the second item in the list (index 1)
# del motorcycles[1]
# print(motorcycles)

# Remove and return the last item from the list
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(f"Deleted motorcycle is {popped_motorcycle}")  # Print the motorcycle that was removed

# Pop the last remaining item and store it in a variable
# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Pop the first item in the list (index 0)
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Recreate the list with four motorcycle brands
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# Remove 'ducati' from the list by value
# motorcycles.remove('suzuki')
print(motorcycles)

# Try to remove 'ducati' again, but it's already removed above
too_expensive = 'ducati'
motorcycles.remove(too_expensive)  # This will cause an error because 'ducati' is not in the list
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# This line will raise an IndexError if the list has fewer than 4 elements
print(motorcycles[3])
