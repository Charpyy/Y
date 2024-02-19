import sqlite3
conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Utilisateurs (
               id INTEGER PRIMARY KEY,
               pseudo TEXT NOT NULL,
               mdp TEXT NOT NULL,
               email TEXT NOT NULL)''')
#cur.execute("INSERT INTO Utilisateurs (pseudo, mdp, email) VALUES (?, ?, ?)", ('Alice', 'mot_de_passe_alice', 'alice@example.com'))
#cur.execute("INSERT INTO Utilisateurs (pseudo, mdp, email) VALUES (?, ?, ?)", ('Bob', 'mot_de_passe_bob', 'bob@example.com'))
#conn.commit()
conn.close()
