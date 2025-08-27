# Create a dictionary to store information about a person
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 28,
    "city": "New York"
}

# Print each piece of information
print("First Name:", person["first_name"])
print("Last Name:", person["last_name"])
print("Age:", person["age"])
print("City:", person["city"])

# Create dictionaries for three people
person1 = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 28,
    "city": "New York"
}

person2 = {
    "first_name": "Alice",
    "last_name": "Smith",
    "age": 32,
    "city": "Los Angeles"
}

person3 = {
    "first_name": "Michael",
    "last_name": "Brown",
    "age": 40,
    "city": "Chicago"
}

# Store all dictionaries in a list
people = [person1, person2, person3]

# Loop through the list and print everything about each person
for person in people:
    print(f"\nFirst Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
