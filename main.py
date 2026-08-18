from add import add_song
from delete import delete_song

playlists = []
songs = []

def create_playlist(playlists_list, songs_list):
    name = input("Enter playlist name: ")
    if name != "":
        new_playlist = {
            "name": name,
            "songs": []
        }
        playlists_list.append(new_playlist)
        print(f"Playlist '{name}' created successfully!")
        
        if songs_list:
            add_choice = input("Do you want to add an existing song to this playlist? (y/n): ")
            if add_choice == "y" or add_choice == "Y":
                print("\nAvailable Songs:")
                for idx, song in enumerate(songs_list, 1):
                    print(f"{idx}. {song['title']} - {song['artist_name']}")
                
                song_num = input("Enter song number to add: ")
                if song_num.isdigit():
                    song_index = int(song_num) - 1
                    if 0 <= song_index < len(songs_list):
                        new_playlist["songs"].append(songs_list[song_index])
                        print(f"Added '{songs_list[song_index]['title']}' to '{name}'!")
                    else:
                        print("Invalid song number.")
                else:
                    print("Invalid input.")
    else:
        print("Playlist name cannot be empty.")

def add_song_to_playlist(songs_list, playlists_list):
    add_song(songs_list)
    
    if songs_list and playlists_list:
        latest_song = songs_list[-1]
        print("\nChoose where to put this song:")
        print("0. Main List Only (No Playlist)")
        for idx, pl in enumerate(playlists_list, 1):
            print(f"{idx}. {pl['name']}")
        
        pl_choice = input("Select playlist number: ")
        if pl_choice.isdigit():
            pl_index = int(pl_choice) - 1
            if pl_index == -1:
                print("Song saved to main list.")
            elif 0 <= pl_index < len(playlists_list):
                playlists_list[pl_index]["songs"].append(latest_song)
                print(f"Added '{latest_song['title']}' to playlist '{playlists_list[pl_index]['name']}'!")
            else:
                print("Invalid playlist selection. Saved to main list only.")

def main():
    while True:
        print("\nPlaylists:")
        if not playlists:
            print("(no playlists yet)")
        else:
            for idx, pl in enumerate(playlists, 1):
                song_count = len(pl['songs'])
                print(f"{idx}. {pl['name']} ({song_count} songs)")
                for song in pl['songs']:
                    print(f"    - {song['title']} by {song['artist_name']}")

        print("\nAll Songs:")
        if not songs:
            print("(empty)")
        else:
            for idx, song in enumerate(songs, 1):
                print(f"{idx}. {song['title']} - {song['artist_name']}")

        print("\n1. Add Song")
        print("2. Delete Song")
        print("3. Create Playlist")
        print("4. Exit")
        choice = input("Select (1/2/3/4): ")

        if choice == "1":
            add_song_to_playlist(songs, playlists)
        elif choice == "2":
            delete_song(songs)
        elif choice == "3":
            create_playlist(playlists, songs)
        elif choice == "4":
            print("Babush")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()