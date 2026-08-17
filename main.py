from add import add_song

songs = []

def main():
    while True:
        print("\nPlaylist:")
        if not songs:
            print("(empty)")
        else:
            count = 1
            for song in songs:
                print(f"{count}. {song['title']} - {song['artist_name']}")
                count += 1

        print("\n1. Add")
        print("2. Exit")
        choice = input("Select (1/2): ")

        if choice == "1":
            add_song(songs)
        elif choice == "2":
            print("Babush")
            break
        else:
            print("Invalid")
main()