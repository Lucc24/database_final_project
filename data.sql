INSERT INTO `artists` (`name`, `genre`, `bio`) VALUES
('The Beatles', 'Rock', 'The Beatles were an English rock band formed in Liverpool in 1960. They are regarded as the most influential band of all time.'),
('Pink Floyd', 'Rock', 'Pink Floyd is an English rock band that achieved worldwide success with their progressive rock music and innovative album covers.'),
('The Rolling Stones', 'Rock', 'The Rolling Stones are an English rock band formed in London in 1962, known for their blues-influenced rock and roll.'),
('David Bowie', 'Rock/Pop', 'David Bowie was an influential English singer-songwriter and musician known for his innovative music and visual presentation.'),
('Queen', 'Rock', 'Queen is a British rock band known for their theatrical performances and anthemic songs featuring Freddie Mercury as lead vocalist.');

INSERT INTO `songs` (`artist_id`, `title`, `bpm`, `duration_seconds`, `release_date`) VALUES
(1, 'Hey Jude', 127, 431, '1968-08-26'),
(1, 'Let It Be', 69, 243, '1970-03-06'),
(1, 'Yesterday', 102, 125, '1965-08-06'),
(2, 'Wish You Were Here', 120, 496, '1975-09-12'),
(2, 'Comfortably Numb', 96, 396, '1979-11-30'),
(2, 'Money', 120, 405, '1973-03-01'),
(3, 'Sympathy for the Devil', 146, 375, '1968-12-06'),
(3, 'Paint It Black', 134, 263, '1966-05-07'),
(3, 'Brown Sugar', 126, 235, '1971-04-23'),
(4, 'Space Oddity', 96, 325, '1969-07-11'),
(4, 'Heroes', 120, 356, '1977-10-21'),
(4, 'Starman', 87, 258, '1972-04-16'),
(5, 'Bohemian Rhapsody', 55, 354, '1975-10-31'),
(5, 'Another One Bites the Dust', 110, 215, '1980-08-22'),
(5, 'Somebody to Love', 100, 295, '1976-11-03');

INSERT INTO `moods` (`mood_name`, `description`) VALUES
('Energetic', 'High energy, upbeat, motivating'),
('Melancholic', 'Sad, emotional, introspective'),
('Romantic', 'Love-focused, sweet, tender'),
('Relaxing', 'Calming, soothing, peaceful'),
('Dark', 'Mysterious, intense, moody'),
('Happy', 'Joyful, cheerful, uplifting'),
('Aggressive', 'Intense, powerful, rebellious');

INSERT INTO `song_moods` (`song_id`, `mood_id`, `intensity_rank`) VALUES
(1, 6, 1),
(1, 1, 2),
(2, 6, 1),
(2, 3, 2),
(3, 2, 1),
(3, 3, 2),
(4, 2, 1),
(4, 4, 2),
(5, 2, 1),
(5, 4, 2),
(6, 5, 1),
(6, 7, 2),
(7, 7, 1),
(7, 5, 2),
(8, 7, 1),
(8, 1, 2),
(9, 1, 1),
(9, 7, 2),
(10, 4, 1),
(10, 5, 2),
(11, 1, 1),
(11, 6, 2),
(12, 5, 1),
(12, 1, 2),
(13, 2, 1),
(13, 5, 2),
(14, 1, 1),
(14, 7, 2),
(15, 3, 1),
(15, 1, 2);

INSERT INTO `playlists` (`playlist_title`, `description`, `created_at`) VALUES
('Classic Rock Hits', 'The best classic rock songs of all time', '2023-01-15 10:30:00'),
('Chill Vibes', 'Relaxing songs for unwinding and meditation', '2023-02-20 14:45:00'),
('Love Songs', 'Romantic songs for a special someone', '2023-03-10 09:15:00'),
('Workout Mix', 'High energy songs to pump you up', '2023-04-05 06:00:00'),
('Late Night Listening', 'Dark and moody songs for the evening', '2023-05-12 20:30:00');

INSERT INTO `playlist_contents` (`playlist_id`, `song_id`, `track_order`) VALUES
(1, 1, 1),
(1, 9, 2),
(1, 13, 3),
(1, 7, 4),
(1, 3, 5),
(2, 4, 1),
(2, 5, 2),
(2, 10, 3),
(3, 2, 1),
(3, 15, 2),
(4, 14, 1),
(4, 9, 2),
(5, 6, 1),
(5, 12, 2),
(5, 11, 3);
