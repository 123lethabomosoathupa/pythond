import matplotlib.pyplot as plt
from random_walk import RandomWalk   # Import the RandomWalk class

while True:
    # Generate a random walk with 50,000 points
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Set up the plot
    plt.style.use('classic')
    fig, ax = plt.subplots()

    # Create a sequence of point numbers for coloring
    point_numbers = range(rw.num_points)

    # Plot all points:
    # - c=point_numbers → color points based on their order
    # - cmap=plt.cm.Blues → color map (light blue to dark blue)
    # - s=1 → very small points for a smooth path
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=1)

    # Alternative simple plot (all points same color/size)
    # ax.scatter(rw.x_values, rw.y_values, s=15)

    # Keep the aspect ratio equal so the walk isn’t stretched
    ax.set_aspect('equal')

    # Highlight the starting point (green) and ending point (red)
    # ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Hide axis ticks and labels for a cleaner look
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Display the plot
    plt.show()

    # Ask user whether to generate another random walk
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
