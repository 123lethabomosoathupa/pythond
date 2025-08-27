class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name   # Dog's name
        self.age = age     # Dog's age in years

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# Create instances of the Dog class
my_dog = Dog('Willie', 6)   # A 6-year-old dog named Willie
your_dog = Dog('Lucy', 3)   # A 3-year-old dog named Lucy

# Display information about my_dog
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()  # Call the sit() method for my_dog

# Display information about your_dog
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()  # Call the sit() method for your_dog
