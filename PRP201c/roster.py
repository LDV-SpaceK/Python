import json
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect(r'X:\CODE\Python\prp202c\rosterdb.sqlite')
cur = conn.cursor()

# Setup the database schema
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

# Prompt for file name
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = r'X:\CODE\Python\prp202c\roster_data.json'

# Read and parse JSON data
with open(fname) as file:
    json_data = json.load(file)

# Process each entry in the JSON data
for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    # Insert or ignore user
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES ( ? )', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    # Insert or ignore course
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES ( ? )', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    # Insert or replace member
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) 
        VALUES ( ?, ?, ? )''', 
        (user_id, course_id, role))

    conn.commit()

# Close the connection
cur.close()
conn.close()
