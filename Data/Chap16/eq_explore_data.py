from pathlib import Path
import json

# --- Load the data ---

# Path to the GeoJSON file containing earthquake data
path = Path('eq_data/eq_data_1_day_m1.geojson')

# Read the entire file as a string
contents = path.read_text(encoding='utf-8')

# Convert the JSON string into a Python dictionary
all_eq_data = json.loads(contents)

# --- Explore the data ---

# 'features' contains a list of all earthquake entries
all_eq_dicts = all_eq_data['features']

# Prepare lists to store magnitudes, longitudes, and latitudes
mags, lons, lats = [], [], []

# Loop through each earthquake entry
for eq_dict in all_eq_dicts:
    # Extract magnitude from properties
    mag = eq_dict['properties']['mag']

    # Extract longitude and latitude from geometry coordinates
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]

    # Append values to the lists
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Print the first few values to check
print(mags[:10])   # First 10 magnitudes
print(lons[:5])    # First 5 longitudes
print(lats[:5])    # First 5 latitudes
