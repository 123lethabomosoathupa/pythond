# 8-14. Cars
def make_car(manufacturer, model, **options):
    car_info = {
        "manufacturer": manufacturer,
        "model": model
    }
    # Add extra keyword arguments to the dictionary
    for key, value in options.items():
        car_info[key] = value
    return car_info

# Example call
car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)

# Another example
car2 = make_car("tesla", "model s", color="red", autopilot=True)
print(car2)
