# Create a list of bicycle brand names
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# Print the entire list of bicycles
print("Print the entire list of bicycles")
print(bicycles)

# Print the first item in the list
print("Print the first item in the list")
print(bicycles[0])

# Print the first item in title case (first letter capitalized)
print("Print the first item in title case (first letter capitalized)")
print(bicycles[0].title())

# Print the second item in the list
print("Print the second item in the list")
print(bicycles[1])

# Print the fourth item in the list
print("Print the fourth item in the list")
print(bicycles[3])

# Print the second-to-last item in the list using negative indexing
print("Print the second-to-last item in the list using negative indexing")
print(bicycles[-2])

# Create a message using the first item in the list and print it
print("Create a message using the first item in the list and print it")
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
