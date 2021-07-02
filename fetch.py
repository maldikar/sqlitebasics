import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("SELECT * FROM customers")
data = c.fetchall()
#fetchone() can used to fetch first row of the database
#fetchmany(n) can be used to fetch first n number of rows
#this will give a list of tuples as output you can use for loops for better visualisation of the data.


conn.commit()

#close our connection
conn.close()

