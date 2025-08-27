# Define a general Car class
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make                # Manufacturer of the car
        self.model = model              # Model name of the car
        self.year = year                # Year the car was made
        self.odometer_reading = 0       # Default odometer reading is set to 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"  # Format car details into one string
        return long_name.title()        # Capitalize each word in the string

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:  # Prevent rolling back the odometer
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


# Define a Battery class for electric cars
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size  # Battery size in kilowatt-hours (kWh)

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150   # Estimated range for a 40 kWh battery
        elif self.battery_size == 65:
            range = 225   # Estimated range for a 65 kWh battery
        print(f"This car can go about {range} miles on a full charge.")


# Define an ElectricCar class, inheriting from Car
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)  # Call the Car class constructor
        self.battery_size = 40               # Default battery size for this electric car
        self.battery = Battery()             # Create a Battery instance as an attribute

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


# Create an instance of ElectricCar
my_leaf = ElectricCar('nissan', 'leaf', 2024)

# Display details about the car
print(my_leaf.get_descriptive_name())     # Prints: "2024 Nissan Leaf"

# Show battery details from ElectricCar method
my_leaf.describe_battery()

# Show battery details from the Battery class directly
my_leaf.battery.describe_battery()

# Show the estimated driving range
my_leaf.battery.get_range()
