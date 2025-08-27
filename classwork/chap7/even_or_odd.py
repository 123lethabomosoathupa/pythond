# Prompt the user to enter a number
number = input("Enter a number, and I'll tell you if it's even or odd: ")

# Convert the input string to an integer
number = int(number)

# Check if the number is divisible by 2 (even)
if number % 2 == 0:
    # If true, print that the number is even
    print(f"\nThe number {number} is even.")
else:
    # If false, print that the number is odd
    print(f"\nThe number {number} is odd.")

