def add_song(songs):
    title = input("Enter song title: ")
    artist_name = input("Enter artist name: ")

    if title:
        songs.append({'title': title, 'artist_name': artist_name})
        print("Song added to playlist")
        print(f"{title} - {artist_name}")
        return 
    else:
        print("error")
