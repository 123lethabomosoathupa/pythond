from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# --- Load the CSV data ---

# Path to the Sitka weather CSV file
path = Path('weather_data/sitka_weather_2021_simple.csv')

# Read all lines from the CSV file
lines = path.read_text().splitlines()

# Create a CSV reader object
reader = csv.reader(lines)

# Extract header row (column names)
header_row = next(reader)

# --- Extract dates, high temperatures, and low temperatures ---

dates, highs, lows = [], [], []

for row in reader:
    # Convert string date to datetime object
    current_date = datetime.strptime(row[2], '%Y-%m-%d')

    # Extract high and low temperatures as integers
    high = int(row[4])
    low = int(row[5])

    # Append to lists
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# --- Plotting section ---

plt.style.use('seaborn-v0_8')  # Use a clean plotting style
fig, ax = plt.subplots()

# Plot highs and lows with transparency
ax.plot(dates, highs, color='red', alpha=0.5, label="Highs")
ax.plot(dates, lows, color='blue', alpha=0.5, label="Lows")

# Shade the area between highs and lows
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)          # X-axis label left empty
fig.autofmt_xdate()                     # Auto-rotate date labels
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

# Optional: add legend
ax.legend()

# Display the plot
plt.show()
