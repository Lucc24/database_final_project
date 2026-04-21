
CREATE TABLE `artists` (
  `artist_id` int AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `genre` varchar(100),
  `bio` text,
  PRIMARY KEY (`artist_id`)
);

CREATE TABLE `songs` (
  `song_id` int AUTO_INCREMENT,
  `artist_id` int,
  `title` varchar(255) NOT NULL,
  `bpm` int,
  `duration_seconds` int,
  `release_date` date,
  PRIMARY KEY (`song_id`)
);

CREATE TABLE `moods` (
  `mood_id` int AUTO_INCREMENT,
  `mood_name` varchar(100) NOT NULL,
  `description` varchar(255),
  PRIMARY KEY (`mood_id`)
);

CREATE TABLE `song_moods` (
  `song_id` int,
  `mood_id` int,
  `intensity_rank` int,
  PRIMARY KEY (`song_id`, `mood_id`),
  FOREIGN KEY (`mood_id`)
      REFERENCES `moods`(`mood_id`)
);

CREATE TABLE `playlists` (
  `playlist_id` int AUTO_INCREMENT,
  `playlist_title` varchar(255) NOT NULL,
  `description` varchar(255),
  `created_at` datetime,
  PRIMARY KEY (`playlist_id`)
);

CREATE TABLE `playlist_contents` (
  `playlist_id` int,
  `song_id` int,
  `track_order` int,
  PRIMARY KEY (`playlist_id`, `song_id`)
);

