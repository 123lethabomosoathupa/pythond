from operator import itemgetter
import requests

# --- Fetch top stories IDs ---

# URL for top stories on Hacker News
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

# Send GET request
r = requests.get(url)
print(f"Status code: {r.status_code}")   # 200 means success

# List of submission IDs for top stories
submission_ids = r.json()

# List to hold dictionaries with story info
submission_dicts = []

# --- Process a subset of submissions (first 5 for demonstration) ---
for submission_id in submission_ids[:5]:
    # URL for individual submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"

    # Send GET request for this submission
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")

    # Convert JSON response to a dictionary
    response_dict = r.json()

    # Build a dictionary containing relevant info
    submission_dict = {
        'title': response_dict['title'],                         # Story title
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",  # Link to discussion
        'comments': response_dict['descendants'],               # Number of comments
    }

    # Add the dictionary to the list
    submission_dicts.append(submission_dict)

# --- Sort submissions by number of comments (descending) ---
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# --- Print the results ---
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
