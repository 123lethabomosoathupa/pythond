import requests
import plotly.express as px

# --- Make an API call to GitHub ---

# URL to search repositories:
# - language:python → only Python projects
# - sort:stars → sort by star count
# - stars:>10000 → only projects with more than 10,000 stars
url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"

# Headers to use GitHub API v3
headers = {"Accept": "application/vnd.github.v3+json"}

# Send GET request
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")  # 200 = success

# --- Process the response ---

response_dict = r.json()  # Convert JSON to Python dict
print(f"Complete results: {not response_dict['incomplete_results']}")  # Check if results are complete

# Extract repository items
repo_dicts = response_dict['items']

# Prepare lists for visualization
repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    # Repository name and URL
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"  # Make clickable links
    repo_links.append(repo_link)

    # Star count
    stars.append(repo_dict['stargazers_count'])

    # Hover text: owner + description
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# --- Create the Plotly bar chart ---

title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}

fig = px.bar(
    x=repo_links,
    y=stars,
    title=title,
    labels=labels,
    hover_name=hover_texts
)

# Customize chart layout
fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20
)

# Customize bar appearance
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

# Show interactive chart
fig.write_html("py_repo.html")
