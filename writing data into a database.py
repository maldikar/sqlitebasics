import sqlite3


conn = sqlite3.connect('customer.db')


#create cursor
c = conn.cursor()



#write into tables
c.execute("INSERT INTO customers VALUES ('moh','maldik','mohitmaldar@gmail.com')")


#commit our database
conn.commit()

#close our connection
conn.close()
