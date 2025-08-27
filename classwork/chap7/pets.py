pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print("\nOriginal list:", pets)

# Keep removing while either 'cat' or 'dog' is in the list
while 'cat' in pets or 'dog' in pets:
    if 'cat' in pets:
        pets.remove('cat')
    if 'dog' in pets:
        pets.remove('dog')

print("\nUpdated list:", pets)
