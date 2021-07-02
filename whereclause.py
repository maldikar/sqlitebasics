
import sqlite3
name = "mohit"
conn = sqlite3.connect('customer.db')

c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS customers(first_name TEXT,last_name TEXT,email TEXT)""")

c.execute("SELECT * FROM customers WHERE first_name ='mohit'")

data = c.fetchall()

print(data)


conn.commit()

#close our connection
conn.close()
