# Import only the ElectricCar class from the electric_car module
from electric_car import ElectricCar

# Create an ElectricCar object (make, model, year)
my_leaf = ElectricCar('nissan', 'leaf', 2024)

# Display a descriptive name for the car (inherited from Car class)
print(my_leaf.get_descriptive_name())  # Output: "2024 Nissan Leaf"

# Describe the battery using the Battery class inside ElectricCar
my_leaf.battery.describe_battery()     # e.g. "This car has a 40-kWh battery."

# Show the estimated range for the current battery size
my_leaf.battery.get_range()            # e.g. "This car can go about 150 miles on a full charge."
