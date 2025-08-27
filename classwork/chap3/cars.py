# Create a list of car brand names
print("List of car brand names")
cars = ['bmw', 'audi', 'toyota', 'subaru']

# Permanently sort the list in alphabetical order
print("List in alphabetical order")
cars.sort()
print(cars)

# Permanently sort the list in reverse alphabetical order
print("list in reverse alphabetical order")
cars.sort(reverse=True)
# Print the list after permanent reverse sort
print(cars)

# Show that the original list has been permanently changed
print("Here is the original list:")
print(cars)

# Temporarily sort the list in alphabetical order using sorted()
print("\nHere is the sorted list:")
print(sorted(cars))

# Show that the original list is still the same after using sorted()
print("\nHere is the original list again:")
print(cars)

# Reverse the current order of the list (not sorted, just reversed)
print("Reverse the current order of the list (not sorted, just reversed)")
cars.reverse()
print(cars)

# Print the number of items in the list
print("Print the number of items in the list")
print(len(cars))
