# Import the Car class directly from the car module
from car import Car

# Import Car and ElectricCar directly from the electric_car module
from electric_car import Car, ElectricCar

# Import the entire car module (so you access classes as car.ClassName)
import car


# Create a Car object from the 'car' module's Car class (first import)
my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())  # Expected: "2024 Ford Mustang"


# Create an ElectricCar object from the 'electric_car' module
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())     # Expected: "2024 Nissan Leaf"


# Create another Car object
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())  # Expected: "2024 Audi A4"

# Directly set the odometer reading
my_new_car.odometer_reading = 23
my_new_car.read_odometer()  # Expected: "This car has 23 miles on it."


# Create a Car object using the car module (accessing it as car.Car)
my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())  # Expected: "2024 Ford Mustang"

# Create an ElectricCar object using the car module (car.ElectricCar)
my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())     # Expected: "2024 Nissan Leaf"
