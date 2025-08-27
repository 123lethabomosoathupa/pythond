print("\n\tExercise 8.5\n")

# Define the function with a default country
def describe_city(city, country="South Africa"):
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city("Cape Town")              # Uses default country
describe_city("Johannesburg")           # Uses default country
describe_city("Tokyo", "Japan")         # Overrides default

print("\n\tExercise 8.6\n")

# Define the function
def city_country(city, country):
    return f"{city}, {country}"

# Call the function with three city-country pairs and print results
print(city_country("Santiago", "Chile"))
print(city_country("Tokyo", "Japan"))
print(city_country("Cape Town", "South Africa"))
