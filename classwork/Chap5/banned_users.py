# List of users who are banned from posting
banned_users = ['andrew', 'carolina', 'david']

# Current user trying to post
user = 'marie'

# Check if the user is NOT in the banned users list
if user not in banned_users:
    # Allow the user to post a response
    print(f"{user.title()}, you can post a response if you wish.")
