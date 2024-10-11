import sqlite3

conn = sqlite3.connect('database.db')

cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

conn.commit()
 
cur.execute("INSERT INTO users (name,age) VALUES (?,?)", ("Masha", 18))

conn.commit()