#5.3

# Version that passes the if test
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")  # This will print

# Version that fails the if test (no output)
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")  # This will NOT print

#5.4
# Version where the if block runs
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")  # This will print
else:
    print("You just earned 10 points.")  # This won't run

# Version where the else block runs
alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")  # This won't run
else:
    print("You just earned 10 points.")  # This will print
#5.5
# Version with green alien
alien_color = 'green'

if alien_color == 'green':
    print("You earned 5 points.")  # This will print
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

# Version with yellow alien
alien_color = 'yellow'

if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")  # This will print
else:
    print("You earned 15 points.")

# Version with red alien
alien_color = 'red'

if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")  # This will print
