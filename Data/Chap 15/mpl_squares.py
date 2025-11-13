import matplotlib.pyplot as plt   # Import matplotlib for plotting

# Data for plotting
input_values = [1, 2, 3, 4, 5]         # x-values
squares = [1, 4, 9, 16, 25]            # y-values (squares of input_values)

# Choose a style for the plot (seaborn look)
plt.style.use('seaborn-v0_8')

# Create the figure and axes object
fig, ax = plt.subplots()

# Plot the data
ax.plot(input_values, squares, linewidth=3)   # Plot x vs y (main line)
ax.plot(squares, linewidth=3)                 # Plot just y-values (index vs squares)

# Set chart title and labels
ax.set_title("Square Numbers", fontsize=24)   # Chart title
ax.set_xlabel("Value", fontsize=14)           # X-axis label
ax.set_ylabel("Square of Value", fontsize=14) # Y-axis label

# Customize tick label size
ax.tick_params(labelsize=14)

# Display the plot
plt.show()
