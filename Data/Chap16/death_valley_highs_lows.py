from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Path to the CSV weather data
path = Path('weather_data/death_valley_2021_simple.csv')

# Read all lines from the file
lines = path.read_text().splitlines()

# Create a CSV reader object
reader = csv.reader(lines)

# Extract the header row (column names)
header_row = next(reader)

# Prepare lists to hold data
dates, highs, lows = [], [], []

# Extract dates and temperatures from the CSV rows
for row in reader:
    # Convert string date to datetime object
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        # Convert high and low temperatures from strings to integers
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        # Some rows may be missing data (skip them)
        print(f"Missing data for {current_date}")
    else:
        # Store valid data
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# --- Plotting section ---

plt.style.use('seaborn-v0_8')        # Use a clean style
fig, ax = plt.subplots()

# Plot highs and lows with some transparency (alpha)
ax.plot(dates, highs, color='red', alpha=0.5, label="Highs")
ax.plot(dates, lows, color='blue', alpha=0.5, label="Lows")

# Shade the area between high and low temperatures
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)     # Title with two lines
fig.autofmt_xdate()                  # Auto-format x-axis labels (rotate dates)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

# Optional: show legend
ax.legend()

# Display the plot
plt.show()
