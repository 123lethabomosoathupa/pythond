# List of car brands
cars = ['audi', 'bmw', 'subaru', 'toyota']

# Loop through each car in the list
for car in cars:
    # If the car is 'bmw', print it in uppercase
    if car == 'bmw':
        print(car.upper())
    else:
        # Otherwise, print the car name in title case (first letter capitalized)
        print(car.title())
