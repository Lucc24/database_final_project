-- Get all songs by The Beatles
SELECT s.song_id, s.title, s.bpm, s.release_date, a.name
FROM songs s
JOIN artists a ON s.artist_id = a.artist_id
WHERE a.name = 'The Beatles';

-- Get moods for Bohemian Rhapsody
SELECT s.title, m.mood_name
FROM songs s
JOIN song_moods sm ON s.song_id = sm.song_id
JOIN moods m ON sm.mood_id = m.mood_id
WHERE s.title = 'Bohemian Rhapsody';

-- Get all songs in Classic Rock Hits playlist
SELECT pc.track_order, s.title, a.name
FROM playlist_contents pc
JOIN songs s ON pc.song_id = s.song_id
JOIN artists a ON s.artist_id = a.artist_id
JOIN playlists p ON pc.playlist_id = p.playlist_id
WHERE p.playlist_title = 'Classic Rock Hits'
ORDER BY pc.track_order;

-- Get all Relaxing songs
SELECT s.title, a.name, s.bpm
FROM songs s
JOIN artists a ON s.artist_id = a.artist_id
JOIN song_moods sm ON s.song_id = sm.song_id
JOIN moods m ON sm.mood_id = m.mood_id
WHERE m.mood_name = 'Relaxing';

-- Count songs per artist
SELECT a.name, COUNT(s.song_id) as song_count
FROM artists a
LEFT JOIN songs s ON a.artist_id = s.artist_id
GROUP BY a.artist_id, a.name;

-- Find songs between 120-150 BPM
SELECT s.title, a.name, s.bpm
FROM songs s
JOIN artists a ON s.artist_id = a.artist_id
WHERE s.bpm BETWEEN 120 AND 150;

-- Get all playlists and song count
SELECT p.playlist_id, p.playlist_title, COUNT(pc.song_id) as song_count
FROM playlists p
LEFT JOIN playlist_contents pc ON p.playlist_id = pc.playlist_id
GROUP BY p.playlist_id, p.playlist_title, p.description, p.created_at
ORDER BY song_count DESC;

--  Find songs released after 1970 with multiple moods
SELECT 
    s.song_id,
    s.title,
    a.name as artist_name,
    YEAR(s.release_date) as release_year,
    s.duration_seconds,
    GROUP_CONCAT(m.mood_name SEPARATOR ', ') as moods
FROM songs s
JOIN artists a ON s.artist_id = a.artist_id
LEFT JOIN song_moods sm ON s.song_id = sm.song_id
LEFT JOIN moods m ON sm.mood_id = m.mood_id
WHERE YEAR(s.release_date) >= 1970
GROUP BY s.song_id, s.title, a.name, s.release_date, s.duration_seconds
ORDER BY s.release_date DESC;
