import plotly.express as px
from die import Die

# Create two dice:
# - die_1 is a 6-sided die (default)
# - die_2 is a 10-sided die
die_1 = Die()
die_2 = Die(10)

# Roll both dice 50,000 times and store the sums of their rolls
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results:
# - Find the frequency of each possible sum (2 through 16)
frequencies = []
max_result = die_1.num_sides + die_2.num_sides   # Largest possible sum (6+10=16)
poss_results = range(2, max_result+1)            # Possible sums are 2 through 16
for value in poss_results:
    frequency = results.count(value)             # Count how often each sum appears
    frequencies.append(frequency)

# Create a bar chart with Plotly
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Customize chart:
# - Set x-axis to show every integer value (no skipping)
fig.update_layout(xaxis_dtick=1)

# Display the chart in the browser
fig.write_html("dice_visual6d6.html")
