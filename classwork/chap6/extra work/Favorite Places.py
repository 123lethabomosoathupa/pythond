# Create a dictionary of favorite places
favorite_places = {
    "Alice": ["Paris", "New York", "Tokyo"],
    "John": ["Cape Town", "Manchester", "Milan"],
    "Sophia": ["Rome", "Madrid"]
}

# Loop through the dictionary
for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"\t{place}")
