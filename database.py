import mysql.connector
from mysql.connector import Error
from datetime import datetime


def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='music_db',
            user='root',
            password='awesomesauce'
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None


def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()


def add_artist(connection, name, genre, bio):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO artists (name, genre, bio) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, genre, bio))
        connection.commit()
        print(f"Artist '{name}' added")
        return cursor.lastrowid
    except Error as e:
        print(f"Error adding artist: {e}")
        return None
    finally:
        cursor.close()


def add_song(connection, artist_id, title, bpm, duration_seconds, release_date):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO songs (artist_id, title, bpm, duration_seconds, release_date) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (artist_id, title, bpm, duration_seconds, release_date))
        connection.commit()
        print(f"Song '{title}' added")
        return cursor.lastrowid
    except Error as e:
        print(f"Error adding song: {e}")
        return None
    finally:
        cursor.close()


def create_playlist(connection, title, description):
    try:
        cursor = connection.cursor()
        created_at = datetime.now()
        query = "INSERT INTO playlists (playlist_title, description, created_at) VALUES (%s, %s, %s)"
        cursor.execute(query, (title, description, created_at))
        connection.commit()
        print(f"Playlist '{title}' created")
        return cursor.lastrowid
    except Error as e:
        print(f"Error creating playlist: {e}")
        return None
    finally:
        cursor.close()


def add_song_to_playlist(connection, playlist_id, song_id):
    try:
        cursor = connection.cursor()
        
        check_query = "SELECT * FROM playlist_contents WHERE playlist_id = %s AND song_id = %s"
        cursor.execute(check_query, (playlist_id, song_id))
        if cursor.fetchone():
            print("Song already in playlist")
            return False
        
        order_query = "SELECT MAX(track_order) FROM playlist_contents WHERE playlist_id = %s"
        cursor.execute(order_query, (playlist_id,))
        result = cursor.fetchone()
        track_order = (result[0] or 0) + 1
        
        insert_query = "INSERT INTO playlist_contents (playlist_id, song_id, track_order) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (playlist_id, song_id, track_order))
        connection.commit()
        print(f"Song added to playlist")
        return True
    except Error as e:
        print(f"Error adding song to playlist: {e}")
        return False
    finally:
        cursor.close()



def get_all_artists(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM artists ORDER BY name")
        artists = cursor.fetchall()
        cursor.close()
        return artists
    except Error as e:
        print(f"Error: {e}")
        return []


def get_artist_by_id(connection, artist_id):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM artists WHERE artist_id = %s", (artist_id,))
        artist = cursor.fetchone()
        cursor.close()
        return artist
    except Error as e:
        print(f"Error: {e}")
        return None


def get_songs_by_artist(connection, artist_name):
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT s.*, a.name as artist_name FROM songs s JOIN artists a ON s.artist_id = a.artist_id WHERE a.name LIKE %s"
        cursor.execute(query, (f"%{artist_name}%",))
        songs = cursor.fetchall()
        cursor.close()
        return songs
    except Error as e:
        print(f"Error: {e}")
        return []


def get_songs_by_mood(connection, mood_name):
    try:
        cursor = connection.cursor(dictionary=True)
        query = """SELECT DISTINCT s.*, a.name as artist_name, m.mood_name 
                   FROM songs s 
                   JOIN artists a ON s.artist_id = a.artist_id 
                   JOIN song_moods sm ON s.song_id = sm.song_id 
                   JOIN moods m ON sm.mood_id = m.mood_id 
                   WHERE m.mood_name LIKE %s"""
        cursor.execute(query, (f"%{mood_name}%",))
        songs = cursor.fetchall()
        cursor.close()
        return songs
    except Error as e:
        print(f"Error: {e}")
        return []


def get_songs_by_bpm(connection, min_bpm, max_bpm):
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT s.*, a.name as artist_name FROM songs s JOIN artists a ON s.artist_id = a.artist_id WHERE s.bpm BETWEEN %s AND %s"
        cursor.execute(query, (min_bpm, max_bpm))
        songs = cursor.fetchall()
        cursor.close()
        return songs
    except Error as e:
        print(f"Error: {e}")
        return []


def get_all_moods(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM moods")
        moods = cursor.fetchall()
        cursor.close()
        return moods
    except Error as e:
        print(f"Error: {e}")
        return []


def get_all_playlists(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        query = """SELECT p.*, COUNT(pc.song_id) as song_count 
                   FROM playlists p 
                   LEFT JOIN playlist_contents pc ON p.playlist_id = pc.playlist_id 
                   GROUP BY p.playlist_id"""
        cursor.execute(query)
        playlists = cursor.fetchall()
        cursor.close()
        return playlists
    except Error as e:
        print(f"Error: {e}")
        return []


def get_playlist_songs(connection, playlist_id):
    try:
        cursor = connection.cursor(dictionary=True)
        query = """SELECT pc.track_order, s.*, a.name as artist_name 
                   FROM playlist_contents pc 
                   JOIN songs s ON pc.song_id = s.song_id 
                   JOIN artists a ON s.artist_id = a.artist_id 
                   WHERE pc.playlist_id = %s 
                   ORDER BY pc.track_order"""
        cursor.execute(query, (playlist_id,))
        songs = cursor.fetchall()
        cursor.close()
        return songs
    except Error as e:
        print(f"Error: {e}")
        return []


def update_artist(connection, artist_id, name, genre, bio):
    try:
        cursor = connection.cursor()
        query = "UPDATE artists SET name = %s, genre = %s, bio = %s WHERE artist_id = %s"
        cursor.execute(query, (name, genre, bio, artist_id))
        connection.commit()
        print("Artist updated")
        cursor.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False


def update_song(connection, song_id, title, bpm, duration):
    try:
        cursor = connection.cursor()
        query = "UPDATE songs SET title = %s, bpm = %s, duration_seconds = %s WHERE song_id = %s"
        cursor.execute(query, (title, bpm, duration, song_id))
        connection.commit()
        print("Song updated")
        cursor.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False


def delete_song(connection, song_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM playlist_contents WHERE song_id = %s", (song_id,))
        cursor.execute("DELETE FROM song_moods WHERE song_id = %s", (song_id,))
        cursor.execute("DELETE FROM songs WHERE song_id = %s", (song_id,))
        connection.commit()
        print("Song deleted!")
        cursor.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False


def delete_artist(connection, artist_id):
    try:
        cursor = connection.cursor()
        
        cursor.execute("SELECT song_id FROM songs WHERE artist_id = %s", (artist_id,))
        songs = cursor.fetchall()
        
        for (song_id,) in songs:
            cursor.execute("DELETE FROM playlist_contents WHERE song_id = %s", (song_id,))
            cursor.execute("DELETE FROM song_moods WHERE song_id = %s", (song_id,))
        
        cursor.execute("DELETE FROM songs WHERE artist_id = %s", (artist_id,))
        
        cursor.execute("DELETE FROM artists WHERE artist_id = %s", (artist_id,))
        
        connection.commit()
        print("Artist and all songs deleted")
        cursor.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False


def remove_song_from_playlist(connection, playlist_id, song_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM playlist_contents WHERE playlist_id = %s AND song_id = %s", (playlist_id, song_id))
        connection.commit()
        print("Song removed from playlist")
        cursor.close()
        return True
    except Error as e:
        print(f"Error: {e}")
        return False






