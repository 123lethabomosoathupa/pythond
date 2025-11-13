from random import choice

class RandomWalk:
    """A class to generate random walks (random paths on a 2D plane)."""

    def __init__(self, num_points=5000):
        """
        Initialize attributes of the walk.
        - num_points: total number of points in the walk (default 5,000).
        - The walk always starts at (0,0).
        """
        self.num_points = num_points

        # Starting point at the origin
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Generate all the points for the random walk."""

        # Keep moving until we reach the desired number of points
        while len(self.x_values) < self.num_points:

            # Decide the x-direction (1 = right, -1 = left)
            x_direction = choice([1, -1])

            # Decide how far to move in x (0–4 steps)
            x_distance = choice([0, 1, 2, 3, 4])

            # The step is direction * distance
            x_step = x_direction * x_distance

            # Do the same for y-direction (1 = up, -1 = down)
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that don't go anywhere (0,0)
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # Store the new point
            self.x_values.append(x)
            self.y_values.append(y)
