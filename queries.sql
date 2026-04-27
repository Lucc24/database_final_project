
-- get all songs by the beatles and their details
SELECT 
    s.song_id,
    s.title,
    s.bpm,
    s.duration_seconds,
    s.release_date,
    a.name as artist_name,
    a.genre
FROM songs s
JOIN artists a ON s.artist_id = a.artist_id
WHERE a.name = 'The Beatles'
ORDER BY s.release_date DESC;

--Find all moods associated with bohemian rapshody and their intensity
SELECT 
    s.title as song_title,
    a.name as artist_name,
    m.mood_name,
    m.description,
    sm.intensity_rank
FROM songs s
JOIN artists a ON s.artist_id = a.artist_id
JOIN song_moods sm ON s.song_id = sm.song_id
JOIN moods m ON sm.mood_id = m.mood_id
WHERE s.title = 'Bohemian Rhapsody'
ORDER BY sm.intensity_rank ASC;

--  Get the rclassic rock playlist with all song details
SELECT 
    p.playlist_id,
    p.playlist_title,
    p.description,
    pc.track_order,
    s.song_id,
    s.title,
    a.name as artist_name,
    s.duration_seconds,
    s.bpm
FROM playlists p
JOIN playlist_contents pc ON p.playlist_id = pc.playlist_id
JOIN songs s ON pc.song_id = s.song_id
JOIN artists a ON s.artist_id = a.artist_id
WHERE p.playlist_title = 'Classic Rock Hits'
ORDER BY pc.track_order ASC;

-- Find all songs with a relaxibng mood
SELECT 
    s.song_id,
    s.title,
    a.name as artist_name,
    a.genre,
    s.bpm,
    s.duration_seconds,
    m.mood_name,
    sm.intensity_rank
FROM songs s
JOIN artists a ON s.artist_id = a.artist_id
JOIN song_moods sm ON s.song_id = sm.song_id
JOIN moods m ON sm.mood_id = m.mood_id
WHERE m.mood_name = 'Relaxing'
ORDER BY sm.intensity_rank DESC, s.title ASC;

-- Count songs by genre and get artist information
SELECT 
    a.genre,
    a.name as artist_name,
    COUNT(s.song_id) as total_songs,
    AVG(s.bpm) as average_bpm,
    AVG(s.duration_seconds) as average_duration
FROM artists a
LEFT JOIN songs s ON a.artist_id = s.artist_id
GROUP BY a.artist_id, a.genre, a.name
ORDER BY total_songs DESC;

--  Find songs within 120 and 150 BPM 
SELECT 
    s.song_id,
    s.title,
    a.name as artist_name,
    s.bpm,
    s.duration_seconds,
    s.release_date
FROM songs s
JOIN artists a ON s.artist_id = a.artist_id
WHERE s.bpm BETWEEN 120 AND 150
ORDER BY s.bpm DESC;

-- Get all playlists with song count and total duration
SELECT 
    p.playlist_id,
    p.playlist_title,
    p.description,
    p.created_at,
    COUNT(pc.song_id) as song_count,
    SEC_TO_TIME(SUM(s.duration_seconds)) as total_duration,
    ROUND(AVG(s.bpm), 2) as average_bpm
FROM playlists p
LEFT JOIN playlist_contents pc ON p.playlist_id = pc.playlist_id
LEFT JOIN songs s ON pc.song_id = s.song_id
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
