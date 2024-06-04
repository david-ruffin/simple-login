import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        firstname TEXT NOT NULL
    )
''')
conn.commit()
conn.close()
