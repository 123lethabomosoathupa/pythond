import requests
import json

# --- Make an API request ---

# URL for a specific Hacker News item (story, comment, etc.)
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"

# Send a GET request to the API
r = requests.get(url)

# Print the HTTP status code to check if the request was successful
print(f"Status code: {r.status_code}")   # 200 means success

# --- Parse and explore the response ---

# Convert the JSON response to a Python dictionary
response_dict = r.json()

# Pretty-print the dictionary with indentation for readability
response_string = json.dumps(response_dict, indent=4)
print(response_string)
