import database


def show_menu(title, options):
    print(f"  {title}")
    for num, option in options.items():
        print(f"{num}. {option}")
    print()


def get_input(prompt, input_type=str):
    while True:
        try:
            user_input = input(prompt).strip()
            if input_type == int:
                return int(user_input)
            elif input_type == float:
                return float(user_input)
            return user_input
        except ValueError:
            print("Invalid input, try again")


def confirm(prompt):
    response = input(f"{prompt} (yes/no): ").strip().lower()
    return response in ['yes', 'y']


def view_artists(conn):
    artists = database.get_all_artists(conn)
    if not artists:
        print("No artists found")
        return
    print("\nArtists:")
    for artist in artists:
        print(f"  ID: {artist['artist_id']} | {artist['name']} ({artist['genre']})")


def add_artist(conn):
    print("\nAdd New Artist")
    name = get_input("Artist name: ")
    genre = get_input("Genre: ")
    bio = get_input("Description: ")
    database.add_artist(conn, name, genre, bio)


def view_artist_details(conn):
    view_artists(conn)
    artist_id = get_input("\nEnter artist ID: ", int)
    artist = database.get_artist_by_id(conn, artist_id)
    if not artist:
        print("Artist not found")
        return
    
    print(f"\n{artist['name']}")
    print(f"Genre: {artist['genre']}")
    print(f"Description: {artist['bio']}")
    
    songs = database.get_songs_by_artist(conn, artist['name'])
    if songs:
        print(f"\nSongs ({len(songs)}):")
        for song in songs:
            print(f"  - {song['title']} (BPM: {song['bpm']})")


def update_artist(conn):
    view_artists(conn)
    artist_id = get_input("\nEnter artist ID: ", int)
    artist = database.get_artist_by_id(conn, artist_id)
    if not artist:
        print("Artist not found")
        return
    
    name = get_input(f"New name (current: {artist['name']}): ")
    genre = get_input(f"New genre (current: {artist['genre']}): ")
    bio = get_input(f"New description (current: {artist['bio'][:50]}...): ")
    
    database.update_artist(conn, artist_id, name, genre, bio)


def delete_artist(conn):
    view_artists(conn)
    artist_id = get_input("\nEnter artist ID: ", int)
    artist = database.get_artist_by_id(conn, artist_id)
    if not artist:
        print("Artist not found")
        return
    
    if confirm(f"Delete '{artist['name']}' and all their songs?"):
        database.delete_artist(conn, artist_id)


def artist_menu(conn):
    while True:
        show_menu("Artist Management", {
            1: "View All Artists",
            2: "Add New Artist",
            3: "View Artist Details",
            4: "Update Artist",
            5: "Delete Artist",
            6: "Back to Main Menu"
        })
        
        choice = get_input("Choice: ")
        
        if choice == "1":
            view_artists(conn)
        elif choice == "2":
            add_artist(conn)
        elif choice == "3":
            view_artist_details(conn)
        elif choice == "4":
            update_artist(conn)
        elif choice == "5":
            delete_artist(conn)
        elif choice == "6":
            break
        else:
            print("Invalid choice")
        
        input("\nPress Enter to continue")


def add_song(conn):
    print("\nAdd New Song")
    view_artists(conn)
    
    artist_id = get_input("Enter artist ID: ", int)
    if not database.get_artist_by_id(conn, artist_id):
        print("Artist not found")
        return
    
    title = get_input("Song title: ")
    bpm = get_input("BPM: ", int)
    duration = get_input("Duration (seconds): ", int)
    
    year = get_input("Release year (YYYY): ", int)
    month = get_input("Release month (MM): ", int)
    day = get_input("Release day (DD): ", int)
    
    release_date = f"{year}-{month:02d}-{day:02d}"
    database.add_song(conn, artist_id, title, bpm, duration, release_date)


def search_by_artist(conn):
    artist_name = get_input("Artist name: ")
    songs = database.get_songs_by_artist(conn, artist_name)
    
    if not songs:
        print("No songs found")
        return
    
    print(f"\nFound {len(songs)} song(s):")
    for song in songs:
        print(f"  ID: {song['song_id']} | {song['title']} by {song['artist_name']} ({song['bpm']} BPM)")


def search_by_mood(conn):
    moods = database.get_all_moods(conn)
    if moods:
        print("Available moods:")
        for mood in moods:
            print(f"  - {mood['mood_name']}")
    
    mood_name = get_input("\nMood name: ")
    songs = database.get_songs_by_mood(conn, mood_name)
    
    if not songs:
        print("No songs found with that mood")
        return
    
    print(f"\nFound {len(songs)} song(s):")
    for song in songs:
        print(f"  ID: {song['song_id']} | {song['title']} - {song['mood_name']}")


def search_by_bpm(conn):
    min_bpm = get_input("Minimum BPM: ", int)
    max_bpm = get_input("Maximum BPM: ", int)
    
    songs = database.get_songs_by_bpm(conn, min_bpm, max_bpm)
    
    if not songs:
        print("No songs found in that BPM range")
        return
    
    print(f"\nFound {len(songs)} song(s):")
    for song in songs:
        print(f"  ID: {song['song_id']} | {song['title']} by {song['artist_name']} ({song['bpm']} BPM)")


def update_song(conn):
    song_id = get_input("Enter song ID: ", int)
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM songs WHERE song_id = %s", (song_id,))
    song = cursor.fetchone()
    cursor.close()
    
    if not song:
        print("Song not found")
        return
    
    title = get_input(f"New title (current: {song['title']}): ")
    bpm = get_input(f"New BPM (current: {song['bpm']}): ", int)
    duration = get_input(f"New duration (current: {song['duration_seconds']}): ", int)
    
    database.update_song(conn, song_id, title, bpm, duration)


def delete_song(conn):
    song_id = get_input("Enter song ID: ", int)
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT s.*, a.name as artist_name FROM songs s JOIN artists a ON s.artist_id = a.artist_id WHERE s.song_id = %s", (song_id,))
    song = cursor.fetchone()
    cursor.close()
    
    if not song:
        print("Song not found")
        return
    
    if confirm(f"Delete '{song['title']}' by {song['artist_name']}?"):
        database.delete_song(conn, song_id)


def song_menu(conn):
    while True:
        show_menu("Song Management", {
            1: "Add New Song",
            2: "Search by Artist",
            3: "Search by Mood",
            4: "Search by BPM Range",
            5: "Update Song",
            6: "Delete Song",
            7: "Back to Main Menu"
        })
        
        choice = get_input("Choice: ")
        
        if choice == "1":
            add_song(conn)
        elif choice == "2":
            search_by_artist(conn)
        elif choice == "3":
            search_by_mood(conn)
        elif choice == "4":
            search_by_bpm(conn)
        elif choice == "5":
            update_song(conn)
        elif choice == "6":
            delete_song(conn)
        elif choice == "7":
            break
        else:
            print("Invalid choice")
        
        input("\nPress Enter to continue...")


def view_playlists(conn):
    playlists = database.get_all_playlists(conn)
    if not playlists:
        print("No playlists found")
        return
    
    print("\nPlaylists:")
    for playlist in playlists:
        print(f"  ID: {playlist['playlist_id']} | {playlist['playlist_title']} ({playlist['song_count']} songs)")


def create_playlist(conn):
    print("\nCreate New Playlist")
    title = get_input("Playlist title: ")
    description = get_input("Description: ")
    database.create_playlist(conn, title, description)


def view_playlist_songs(conn):
    view_playlists(conn)
    
    playlist_id = get_input("\nEnter playlist ID: ", int)
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM playlists WHERE playlist_id = %s", (playlist_id,))
    playlist = cursor.fetchone()
    cursor.close()
    
    if not playlist:
        print("Playlist not found")
        return
    
    songs = database.get_playlist_songs(conn, playlist_id)
    print(f"\n{playlist['playlist_title']}")
    print(f"Description: {playlist['description']}\n")
    
    if not songs:
        print("No songs in this playlist")
        return
    
    for track in songs:
        print(f"  Track {track['track_order']}: {track['title']} by {track['artist_name']}")


def add_song_to_playlist(conn):
    view_playlists(conn)
    playlist_id = get_input("\nEnter playlist ID: ", int)
    song_id = get_input("Enter song ID: ", int)
    
    database.add_song_to_playlist(conn, playlist_id, song_id)


def remove_song_from_playlist(conn):
    playlist_id = get_input("Enter playlist ID: ", int)
    song_id = get_input("Enter song ID: ", int)
    
    database.remove_song_from_playlist(conn, playlist_id, song_id)


def playlist_menu(conn):
    while True:
        show_menu("Playlist Management", {
            1: "View All Playlists",
            2: "Create New Playlist",
            3: "View Playlist Songs",
            4: "Add Song to Playlist",
            5: "Remove Song from Playlist",
            6: "Back to Main Menu"
        })
        
        choice = get_input("Choice: ")
        
        if choice == "1":
            view_playlists(conn)
        elif choice == "2":
            create_playlist(conn)
        elif choice == "3":
            view_playlist_songs(conn)
        elif choice == "4":
            add_song_to_playlist(conn)
        elif choice == "5":
            remove_song_from_playlist(conn)
        elif choice == "6":
            break
        else:
            print("Invalid choice")
        
        input("\nPress Enter to continue...")


def main():

    print(" song management")

    
    conn = database.create_connection()
    
    if not conn:
        print("could not connect to database")
        return
    
    try:
        while True:
            show_menu("Main Menu", {
                1: "Artist Management",
                2: "Song Management",
                3: "Playlist Management",
                4: "Exit"
            })
            
            choice = get_input("Choice: ")
            
            if choice == "1":
                artist_menu(conn)
            elif choice == "2":
                song_menu(conn)
            elif choice == "3":
                playlist_menu(conn)
            elif choice == "4":
                if confirm("Are you sure you want to exit?"):
                    break
            else:
                print("Invalid choice")
    except KeyboardInterrupt:
        print("\nGoodbye")
    finally:
        database.close_connection(conn)

if __name__ == "__main__":
    main()

