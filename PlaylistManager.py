songs = ["Queen - Bohemian Rhapsody",
        "Michael Jackson - Billie Jean",
        "Nirvana - Smells Like Teen Spirit",
        "The Police - Every Breath You Take",
        "Fleetwood Mac - Dreams",
        "Bob Dylan - Like a Rolling Stone",
        "Aretha Franklin - Respect",
        "The Beatles - Yesterday",
        "Marvin Gaye - What's Going On",
        "The Weeknd - Blinding Lights"]

playlists = []

def welcome():
    choice = input("SongSearch: Playlist Manager\nEnter 1 to create a playlist\nEnter 2 to view playlists\nEnter 3 to exit")
def new_playlist():
    playlist = input("Enter playlist name: ")
    playlists.append(new_playlist)
    print(f"Playlist {playlist} created!")
    print("Add songs\nFor you\n")
    for song in songs:
        print(song)
    welcome()

    if choice == "1":
        new_playlist()
    elif choice == "2":
        for playlist in playlists:
            print(playlist)
    elif choice == "3":
        exit()
    else:
        print("Invalid choice!")

while True:
    welcome()