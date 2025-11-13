from pathlib import Path
import json
import plotly.express as px

# --- Load earthquake data ---

# Path to the GeoJSON file containing earthquakes for the past 30 days
path = Path('eq_data/eq_data_30_day_m1.geojson')

# Read the file as a string
contents = path.read_text(encoding='utf-8')

# Convert JSON string into a Python dictionary
all_eq_data = json.loads(contents)

# --- Extract relevant data from each earthquake entry ---

# 'features' contains a list of all earthquake entries
all_eq_dicts = all_eq_data['features']

# Prepare lists to store earthquake properties
mags, lons, lats, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']                # Magnitude
    lon = eq_dict['geometry']['coordinates'][0]       # Longitude
    lat = eq_dict['geometry']['coordinates'][1]       # Latitude
    eq_title = eq_dict['properties']['title']         # Title (location + magnitude)

    # Append values to lists
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

# --- Create the Plotly scatter_geo map ---

title = 'Global Earthquakes'

fig = px.scatter_geo(
    lat=lats,                  # Latitude coordinates
    lon=lons,                  # Longitude coordinates
    size=mags,                 # Bubble size proportional to magnitude
    title=title,
    color=mags,                # Color points by magnitude
    color_continuous_scale='Viridis',   # Color scale
    labels={'color':'Magnitude'},       # Legend label
    projection='natural earth',         # Map projection style
    hover_name=eq_titles,               # Show earthquake title on hover
)

# Show the interactive map
fig.write_html("world_map.html")

