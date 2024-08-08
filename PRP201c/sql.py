import sqlite3

# Connect to the SQLite database (creates the file if it does not exist)
conn = sqlite3.connect(r"X:\CODE\Python\prp202c\emaildb.sqlite")
cur = conn.cursor()

# Drop the table if it already exists
cur.execute('DROP TABLE IF EXISTS Counts')

# Create the Counts table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Prompt for the file name
fname = input('Enter file name: ')
if len(fname) < 1: fname = 'mbox.txt'

# Try opening the file, handle errors if the file is not found
try:
    fh = open(fname)
except FileNotFoundError:
    print(f"File {fname} not found.")
    exit()

# Regular expression to extract domain from email
import re
domain_pattern = re.compile('@(.+)$')

# Process each line in the file
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    
    # Extract the domain from the email address
    match = domain_pattern.search(email)
    if match:
        domain = match.group(1)
        
        # Check if the domain is already in the database
        cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
        row = cur.fetchone()
        
        if row is None:
            # Insert new domain
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
        else:
            # Update existing domain count
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))
        # Commit all changes at once
        conn.commit()


# Query to get the top 10 organizations
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# Print the results
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the cursor and connection
cur.close()
