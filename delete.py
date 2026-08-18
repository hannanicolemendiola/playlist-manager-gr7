def delete_song(songs):
    if not songs:
        print("Your playlist is empty. Nothing to delete!")
        return

    choice = input("Enter the number of the song you want to delete: ")

    if choice.isdigit():
        index = int(choice) - 1

        if 0 <= index < len(songs):
            removed_song = songs.pop(index)
            print(f"Removed: '{removed_song['title']}' by {removed_song['artist_name']}")
        else:
            print("Error: Invalid song number.")
    else:
        print("Error: Please enter a valid number.")