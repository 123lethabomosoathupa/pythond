# Store the visitor's age
age = 12

# Determine admission cost based on age
if age < 4:
    # Free admission for children under 4
    print("Your admission cost is $0.")
elif age < 18:
    # Discounted admission for people under 18
    print("Your admission cost is $25.")
else:
    # Full price for adults 18 and older
    print("Your admission cost is $40.")


# Check the person's age and determine the admission price
if age < 4:
    # Free admission for children under 4
    price = 0
elif age < 18:
    # Discounted admission for children and teens under 18
    price = 25
else:
    # Full price for adults 18 and over
    price = 40

# Print the final admission cost
print(f"Your admission cost is ${price}.")
