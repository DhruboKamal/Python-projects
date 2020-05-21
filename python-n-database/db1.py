import sqlite3
conn= sqlite3.connect('Music.sqlite')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks(title TEXT,plays INTEGER)')

conn.close()
