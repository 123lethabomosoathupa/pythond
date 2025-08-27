# Create dictionaries for different pets
pet1 = {
    "animal": "dog",
    "owner": "Alice"
}

pet2 = {
    "animal": "cat",
    "owner": "John"
}

pet3 = {
    "animal": "parrot",
    "owner": "Sophia"
}

pet4 = {
    "animal": "rabbit",
    "owner": "Liam"
}

# Store all pet dictionaries in a list
pets = [pet1, pet2, pet3, pet4]

# Loop through the list and print everything about each pet
for pet in pets:
    print(f"\nAnimal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner'].title()}")
