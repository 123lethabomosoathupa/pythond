# Initialize current_number to 1
current_number = 1

# This loop prints numbers from 1 to 5
while current_number <= 5:
    print(current_number)
    current_number += 1  # Increase current_number by 1 in each iteration

# Reset current_number to 0
current_number = 0

# This loop prints odd numbers from 1 to 9
while current_number < 10:
    current_number += 1  # Increment first
    if current_number % 2 == 0:
        continue  # Skip even numbers
    print(current_number)

# Initialize x to 1
x = 1

# This loop prints numbers from 1 to 5
while x <= 5:
    print(x)
    x += 1  # Increment x by 1

# This loop runs forever because x is never updated inside the loop
x = 1
while x <= 5:
    print(x)  # x will always be 1, so this causes an infinite loop
