#Exercise 3.1
# Store the names of a few friends in a list
names = ["Alice", "Brian", "Cindy", "David"]

# Print each name one by one
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#Exercise 3.2

# Using the same list from Exercise 3-1
names = ["Alice", "Brian", "Cindy", "David"]

# Print a personalized greeting for each friend
print(f"Hello {names[0]}, I hope you're having a great day!")
print(f"Hello {names[1]}, I hope you're having a great day!")
print(f"Hello {names[2]}, I hope you're having a great day!")
print(f"Hello {names[3]}, I hope you're having a great day!")

#Exercise 3.3

# List of favorite modes of transportation
vehicles = ["Toyota Hilux", "Honda motorcycle", "Tesla Model 3", "BMW M3"]

# Print a statement about each one
print(f"I would like to own a {vehicles[0]}.")
print(f"I would like to own a {vehicles[1]}.")
print(f"I would like to own a {vehicles[2]}.")
print(f"I would like to own a {vehicles[3]}.")

#Exercise 3.4

# Create a list of guests you'd like to invite to dinner
guests = ["Nelson Mandela", "Ada Lovelace", "Elon Musk"]

# Print a personalized invitation for each guest
print(f"Dear {guests[0]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests[1]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests[2]}, I would be honored to have you join me for dinner.")

#Exercise 3.5

# Original guest list
guests = ["Nelson Mandela", "Ada Lovelace", "Elon Musk"]

# One guest can't make it
print(f"\nUnfortunately, {guests[1]} can't make it to dinner.")

# Replace the unavailable guest with a new guest
guests[1] = "Marie Curie"

# Print new set of invitations
print("\nUpdated Guest List Invitations:")
print(f"Dear {guests[0]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests[1]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests[2]}, I would be honored to have you join me for dinner.")

#Exercise 3.6

# Inform that a bigger table is available
print("\nGood news! We found a bigger table and can invite more guests.")

# Add guests using insert() and append()
guests.insert(0, "Albert Einstein")              # Beginning
guests.insert(2, "Leonardo da Vinci")            # Middle
guests.append("Oprah Winfrey")                   # End

# Print new set of invitations
print("\nNew Guest List Invitations:")
for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")

#Exercise 3.7

# Bad news: only two guests can be invited
print("\nUnfortunately, the new dinner table won’t arrive in time. I can only invite two people.")


removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can’t invite you to dinner this time.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can’t invite you to dinner this time.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can’t invite you to dinner this time.")


# Confirm remaining guests are still invited
print("\nGuests still invited:")
print(f"{guests[0]}, you're still invited to dinner.")
print(f"{guests[1]}, you're still invited to dinner.")


# Empty the list
del guests[0]
del guests[0]

# Confirm list is empty
print("\nFinal guest list:", guests)
 
 
#Exercise 3.8

# List of places to visit (not in alphabetical order)
places = ["Tokyo", "Paris", "New York", "Cape Town", "Sydney"]

# Print the list in original order
print("Original list:")
print(places)

# Print the list in alphabetical order without modifying the original list
print("\nAlphabetical order (using sorted()):")
print(sorted(places))

# Show the original list is unchanged
print("\nOriginal list after sorted():")
print(places)

# Print the list in reverse alphabetical order without modifying the original list
print("\nReverse alphabetical order (using sorted() with reverse=True):")
print(sorted(places, reverse=True))

# Show the original list is still unchanged
print("\nOriginal list after reverse sorted():")
print(places)

# Use reverse() to reverse the order of the original list
places.reverse()
print("\nList after reverse():")
print(places)

# Use reverse() again to restore the original order
places.reverse()
print("\nList after reversing again:")
print(places)

# Use sort() to sort the list in alphabetical order permanently
places.sort()
print("\nList after sort():")
print(places)

# Use sort() with reverse=True to sort the list in reverse alphabetical order permanently
places.sort(reverse=True)
print("\nList after sort(reverse=True):")
print(places)


#Exercise 3.9

# Guest list from previous exercises
guests = ["Nelson Mandela", "Marie Curie", "Elon Musk"]

# Print the number of people invited to dinner
print(f"\nI am inviting {len(guests)} people to dinner.")


#Exercise 3.10

# List of programming languages
languages = ["Python", "JavaScript", "C++", "Java", "Go"]

# Print original list
print("Original list:")
print(languages)

# sorted() - alphabetically, without changing original list
print("\nSorted list:")
print(sorted(languages))

# sorted() reverse alphabetical, without changing original list
print("\nSorted list (reverse):")
print(sorted(languages, reverse=True))

# reverse() - reverses the list permanently
languages.reverse()
print("\nList after reverse():")
print(languages)

# reverse() again to restore original order
languages.reverse()
print("\nList after reversing again:")
print(languages)

# sort() - sorts list permanently in alphabetical order
languages.sort()
print("\nList after sort():")
print(languages)

# sort() with reverse=True - sorts permanently in reverse alphabetical order
languages.sort(reverse=True)
print("\nList after sort(reverse=True):")
print(languages)

# len() - prints the number of items in the list
print(f"\nThere are {len(languages)} languages in the list.")

# append() - add an item to the end
languages.append("Ruby")
print("\nList after append('Ruby'):")
print(languages)

# insert() - add an item at a specific position
languages.insert(2, "Rust")
print("\nList after insert('Rust' at index 2):")
print(languages)

# pop() - remove the last item and print it
popped_language = languages.pop()
print(f"\nPopped language: {popped_language}")
print("List after pop():")
print(languages)

# del - delete an item by index (e.g., delete item at index 1)
del languages[1]
print("\nList after deleting item at index 1:")
print(languages)

#Exercise 3.11

# List of friends
friends = ["Alice", "Brian", "Cindy"]

# Intentionally using an index that doesn't exist (index 3, but list has indices 0-2)
print(friends[3])  # This will cause an IndexError
