# ----------- Car class -----------
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make                    # Manufacturer
        self.model = model                  # Model name
        self.year = year                    # Year of manufacture
        self.odometer_reading = 0           # Mileage starts at 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:  # Prevent rolling back
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


# ----------- Battery class for Electric Cars -----------
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size  # Battery size in kilowatt-hours

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


# ----------- ElectricCar class inheriting from Car -----------
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class and ElectricCar-specific features."""
        super().__init__(make, model, year)  # Initialize Car attributes
        self.battery_size = 40               # Default battery size
        self.battery = Battery()              # Create a Battery instance

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


# ----------- Example usage -----------

# Create a regular car
my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())    # Show car details
my_used_car.update_odometer(23_500)          # Set mileage
my_used_car.read_odometer()
my_used_car.increment_odometer(100)          # Add 100 miles
my_used_car.read_odometer()

# Create another car
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# Create an electric car
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()                   # From ElectricCar class
my_leaf.battery.describe_battery()           # From Battery class
my_leaf.battery.get_range()                  # Show driving range
