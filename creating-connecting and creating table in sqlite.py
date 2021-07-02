import sqlite3


conn = sqlite3.connect('customer.db')

#create cursor
c = conn.cursor()

#create a table
#type of data entered here is TEXT for all 3 entries other data types accepted in sqlite are: NULL, INTEGER, BLOB and REAL 
c.execute("""CREATE TABLE IF NOT EXISTS customers(first_name TEXT,last_name TEXT,email TEXT)""")

#write into tables
c.execute("INSERT INTO customers VALUES ('moh','maldik','mohitmaldar@gmail.com')")





#commit our database
conn.commit()

#close our connection
conn.close()







