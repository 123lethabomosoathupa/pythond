from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# --- Load the CSV data ---

# Path to the Sitka weather CSV file
path = Path('weather_data/sitka_weather_2021_simple.csv')

# Read all lines from the file
lines = path.read_text().splitlines()

# Create a CSV reader
reader = csv.reader(lines)

# Extract header row (column names)
header_row = next(reader)

# --- Extract dates and high temperatures ---

dates, highs = [], []

for row in reader:
    # Convert string date to datetime object
    current_date = datetime.strptime(row[2], '%Y-%m-%d')

    # Extract high temperature as integer
    high = int(row[4])

    # Append to lists
    dates.append(current_date)
    highs.append(high)

# --- Plotting section ---

plt.style.use('seaborn-v0_8')  # Set a clean style
fig, ax = plt.subplots()

# Plot high temperatures as a red line
ax.plot(dates, highs, color='red')

# Format plot
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)           # Leave x-axis label empty
fig.autofmt_xdate()                      # Rotate date labels automatically
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)             # Set tick label size

# Display the plot
plt.show()
