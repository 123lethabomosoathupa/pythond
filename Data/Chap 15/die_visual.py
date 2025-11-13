import plotly.express as px   # Import Plotly Express for creating charts
from die import Die           # Import the custom Die class

# Create one D6 die (a standard six-sided die).
die = Die()

# Roll the die 1,000 times and save each outcome.
results = []
for roll_num in range(1000):
    result = die.roll()       # Roll once
    results.append(result)    # Store the result in the list

# Analyze the results:
# - Count how many times each face value (1–6) appears.
frequencies = []
poss_results = range(1, die.num_sides+1)   # Possible results: 1 through 6
for value in poss_results:
    frequency = results.count(value)       # Count occurrences of this value
    frequencies.append(frequency)

# Visualize the results as a bar chart.
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Show the chart in the browser or notebook.
fig.write_html("die_visual.html")

