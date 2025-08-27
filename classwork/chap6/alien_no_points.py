alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])  # ❌ This will cause a KeyError

# Try to get the value for 'points'; if it doesn't exist, return a default message
point_value = alien_0.get('points', 'No point value assigned.')

# Print the result
print(point_value)