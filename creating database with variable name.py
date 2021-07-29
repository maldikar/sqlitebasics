import sqlite3

a  = 'mohit.db'
conn = sqlite3.connect(a)
c = conn.cursor()

conn.commit()
conn.close()