# Ask the user to input their height in centimeters
height = input("How tall are you, in centimeters? ")

# Convert the input from a string to an integer
height = int(height)

# Check if the height is 144 cm or more
if height >= 144:
    # If yes, the person is tall enough to ride
    print("\nYou're tall enough to ride!")
else:
    # If not, the person needs to grow a bit more to ride
    print("\nYou'll be able to ride when you're a little older.")
