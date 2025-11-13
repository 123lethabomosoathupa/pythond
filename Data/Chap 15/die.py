from random import randint

class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """
        Initialize a die.
        By default, it's a 6-sided die, but you can specify a different number.
        Example: Die(10) creates a 10-sided die (D10).
        """
        self.num_sides = num_sides

    def roll(self):
        """
        Simulate rolling the die.
        Returns a random integer between 1 and the number of sides.
        Example: if num_sides = 6, returns a value from 1 to 6.
        """
        return randint(1, self.num_sides)
