# 8-12. Sandwiches
def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!")

# Call the function with different numbers of arguments
make_sandwich("ham", "cheese")
make_sandwich("turkey", "lettuce", "tomato", "mayo")
make_sandwich("peanut butter", "jelly")
