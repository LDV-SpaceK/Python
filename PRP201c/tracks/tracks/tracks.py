import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect(r"X:\CODE\Python\prp202c\tracks\tracks\trackdb.sqlite")
cur = conn.cursor()

# Create tables and drop existing ones
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')

# Open and process the CSV file
with open(r"X:\CODE\Python\prp202c\tracks\tracks\tracks.csv") as handle:
    for line in handle:
        line = line.strip()
        pieces = line.split(',')
        if len(pieces) < 6:
            continue
        
        name = pieces[0]
        artist = pieces[1]
        album = pieces[2]
        count = pieces[3]
        rating = pieces[4]
        length = pieces[5]
        genre = pieces[6]  # Assuming genre is the 7th column in the CSV

        # Print to verify correct data parsing
        print(name, artist, album, genre, count, rating, length)

        # Insert or ignore Artist
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES ( ? )', (artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
        artist_id = cur.fetchone()[0]

        # Insert or ignore Genre
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES ( ? )', (genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
        genre_id = cur.fetchone()[0]

        # Insert or ignore Album
        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
        album_id = cur.fetchone()[0]

        # Insert or replace Track
        cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, genre_id, len, rating, count) 
            VALUES ( ?, ?, ?, ?, ?, ? )''', 
            (name, album_id, genre_id, length, rating, count))

        conn.commit()

cur.close()
conn.close()
