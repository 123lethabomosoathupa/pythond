print("\n\tExercise 8.7\n")

# 8-7. Album
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

# Create and print three albums without number of songs
print(make_album("Taylor Swift", "Midnights"))
print(make_album("Ed Sheeran", "Divide"))
print(make_album("Adele", "30"))

# Create and print an album with number of songs
print(make_album("Coldplay", "Parachutes", songs=10))

print("\n\tExercise 8.8\n")
# 8-8. User Albums
print("\nEnter album details (type 'quit' at any time to exit):")

while True:
    artist = input("Artist name: ")
    if artist.lower() == "quit":
        break
    
    title = input("Album title: ")
    if title.lower() == "quit":
        break
    
    songs_input = input("Number of songs (optional, press Enter to skip): ")
    if songs_input.lower() == "quit":
        break
    
    if songs_input.isdigit():
        album_info = make_album(artist, title, songs=int(songs_input))
    else:
        album_info = make_album(artist, title)
    
    print(album_info)
