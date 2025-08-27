print("\n---------5.1---------")

# 5 tests that evaluate to True
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

color = 'blue'
print("\nIs color == 'blue'? I predict True.")
print(color == 'blue')

age = 25
print("\nIs age >= 18? I predict True.")
print(age >= 18)

name = 'Alice'
print("\nIs name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')

is_active = True
print("\nIs is_active == True? I predict True.")
print(is_active == True)

# 5 tests that evaluate to False
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs color != 'blue'? I predict False.")
print(color != 'blue')

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs name == 'Bob'? I predict False.")
print(name == 'Bob')

print("\nIs is_active == False? I predict False.")
print(is_active == False)

print("\n------5.2---------")
# 5-2. More Conditional Tests

# --- Tests for equality and inequality with strings ---
fruit = 'apple'
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("\nIs fruit != 'apple'? I predict False.")
print(fruit != 'apple')

# --- Tests using the lower() method ---
name = 'Alice'
print("\nIs name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')

print("\nIs name.lower() == 'ALICE'? I predict False.")
print(name.lower() == 'ALICE')

# --- Numerical tests ---
age = 20
print("\nIs age == 20? I predict True.")
print(age == 20)

print("\nIs age != 20? I predict False.")
print(age != 20)

print("\nIs age > 18? I predict True.")
print(age > 18)

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs age >= 20? I predict True.")
print(age >= 20)

print("\nIs age <= 19? I predict False.")
print(age <= 19)

# --- Tests using and/or ---
height = 170
weight = 65

print("\nIs height > 160 and weight < 70? I predict True.")
print(height > 160 and weight < 70)

print("\nIs height > 180 and weight < 70? I predict False.")
print(height > 180 and weight < 70)

print("\nIs height > 180 or weight < 70? I predict True.")
print(height > 180 or weight < 70)

print("\nIs height < 160 or weight > 70? I predict False.")
print(height < 160 or weight > 70)

# --- Test whether item is in a list ---
colors = ['red', 'green', 'blue']
print("\nIs 'green' in colors? I predict True.")
print('green' in colors)

print("\nIs 'yellow' in colors? I predict False.")
print('yellow' in colors)

# --- Test whether item is not in a list ---
print("\nIs 'yellow' not in colors? I predict True.")
print('yellow' not in colors)

print("\nIs 'blue' not in colors? I predict False.")
print('blue' not in colors)
