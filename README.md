# Vibe Check Archive 
The **Vibe Check Archive** is an advanced music database and analytics tool designed to go beyond just having random lists of songs. While standard streaming services often treat playlists as a basic collection of songs, this archive utilizes detailed metadata, including **BPM (Beats Per Minute)**, **release dates**, and **mood intesity**, in order to help users create the perfect atmosphere for any time of day or event.
---
## Entity Relationship Diagram (ERD)
The following diagram shows the structure of the database, highlighting how artists, songs, moods, and playlists are related to provide a deeper insight into the music.

![Vibe Check Archive ERD](Database%20ER%20diagram%20(crow's%20foot)%20(2).png)

---
## Database Schema
The datbase consists of six core tables that organize musical data and user created collections.

+ **Artists**- This tracks the creators behind the music, including Name, Genre, and Bio.
+ **Songs**- This is the heart of the database, storing the technical data like tempo(BPM), length, and the release dates.
+ **Moods**- A main list of descriptive vibes used to filter the music library.
+ **Playlists**- This Stores the metadata for custom built collections, documenting when and why they were created. 
+ **Song_moods**- A system that allows stacking multiple moods onto a single song with specific intensity ranks
+ **Playlist_contents**- Organizes songs into specific playlists while maintaing the intended track order

---
## Features 
The Vibe Check Archive Python application provides the following capabilities:
+ **Comprehensive Artist Management**: Full ability to add, view details, update profiles, and delete artists. 
+ **Multi-Criteria Song Discovery**: Search and filter the libary by specific Artist names, Mood types, or precise BPM ranges for chill or high energy sessions.
+ **Dynamic Playlist Curation**- Create named playlists with custom descriptions and mangage tracklists by adding or removing songs with automated track ordering.

--- 
## Setup Instructions 

### Requirements
+ Python 3.x
+ MySQL server

### Installation 
1. Clone the Repository 
    * `https://github.com/Lucc24/database_final_project.git`
2. Install the dependencies 
3. Initialize the Database:
    * Execute `schema.sql` to create the table structures.
    * Execute `data.sql` to populate the archive with initial artist and song data.
4. Run the application 

--- 
## Example Usage 
![](pic1.png)
![](pic2.png)
![](pic3.png)
--- 
## Known Bugs & Limitations
+ **Connection Config**: The database credentials such as host, user, and password, are currently hardcodedin database.py and may need to be manually updated for different local environments. 
+ **Date Formatting**: The application requires release dates to be entered as separate integerinputs for Year, Month, and Day.
+ **Single Artist Limit**: The current schema links a song to exactly one artist; it does not currently featured artists or collaborations as separate entities. 
--- 
## Reflection
Creating the **Vibe Check Archive** provided a deep dive into the complexities of relational database design, specifically regarding many-to-many relationships. One of the prmary challenges was managing the **song_moods** and **playlist_contents tables. Ensuring that a signle song could reflect multiple vibes while still maintaining a specific order within a playlist required careful application of primary and foreign keys to maintain the integrity of the data. Beyond the technical setup, this projec highted the calue of metadata in user experience. Moving from a simple list to an archive where you can query for things like Dark and Moody songs released after 1970 showed how structured data can transform how we interact with media. We learned that the why behind a playlist is just as important as the songs themselves, which lead us to include detailed descriptions and timestamps in the schema. 

## File Structure
* `schema.sql`: Table creation scripts.
* `data.sql`: Sample data and initial seeds.
* `queries.sql`: Example SQL queries for testing.
* `main.py`: The primary CLI application entry point.
* `database.py`: Contains all Python functions for database interaction.
* `requirements.txt`: List of Python dependencies.