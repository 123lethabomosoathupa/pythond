import matplotlib.pyplot as plt

# Generate data
x_values = range(1, 1001)               # Numbers 1 through 1000
y_values = [x**2 for x in x_values]     # Squares of those numbers

# Choose a plotting style
plt.style.use('seaborn-v0_8')

# Create figure and axes
fig, ax = plt.subplots()

# Create scatter plot:
# - x_values on x-axis
# - y_values on y-axis
# - c=y_values → color points based on their y-value (squares)
# - cmap=plt.cm.Blues → blue gradient colormap
# - s=10 → small point size
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and axis labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Define the axis ranges (manual limits for clarity)
# X: from 0 to 1100
# Y: from 0 to 1,100,000
ax.axis([0, 1100, 0, 1_100_000])

# Use plain numbers on y-axis (instead of scientific notation)
ax.ticklabel_format(style='plain')

# Customize tick label sizes
ax.tick_params(labelsize=14)

# Display the plot
plt.show()
